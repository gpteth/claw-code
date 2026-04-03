from __future__ import annotations

import argparse

from .bootstrap_graph import build_bootstrap_graph
from .command_graph import build_command_graph
from .commands import execute_command, get_command, get_commands, render_command_index
from .direct_modes import run_deep_link, run_direct_connect
from .i18n import detect_locale, set_locale, t
from .parity_audit import run_parity_audit
from .permissions import ToolPermissionContext
from .port_manifest import build_port_manifest
from .query_engine import QueryEnginePort
from .remote_runtime import run_remote_mode, run_ssh_mode, run_teleport_mode
from .runtime import PortRuntime
from .session_store import load_session
from .setup import run_setup
from .tool_pool import assemble_tool_pool
from .tools import execute_tool, get_tool, get_tools, render_tool_index


def build_parser(lang: str | None = None) -> argparse.ArgumentParser:
    if lang:
        set_locale(lang)
    else:
        set_locale(detect_locale())

    parser = argparse.ArgumentParser(description=t('app.description'))
    parser.add_argument('--lang', choices=['en', 'zh', 'hi', 'es', 'fr'],
                        default=None, help=t('label.language_help'))
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser('summary', help=t('cmd.summary.help'))
    subparsers.add_parser('manifest', help=t('cmd.manifest.help'))
    subparsers.add_parser('parity-audit', help=t('cmd.parity_audit.help'))
    subparsers.add_parser('setup-report', help=t('cmd.setup_report.help'))
    subparsers.add_parser('command-graph', help=t('cmd.command_graph.help'))
    subparsers.add_parser('tool-pool', help=t('cmd.tool_pool.help'))
    subparsers.add_parser('bootstrap-graph', help=t('cmd.bootstrap_graph.help'))
    list_parser = subparsers.add_parser('subsystems', help=t('cmd.subsystems.help'))
    list_parser.add_argument('--limit', type=int, default=32)

    commands_parser = subparsers.add_parser('commands', help=t('cmd.commands.help'))
    commands_parser.add_argument('--limit', type=int, default=20)
    commands_parser.add_argument('--query')
    commands_parser.add_argument('--no-plugin-commands', action='store_true')
    commands_parser.add_argument('--no-skill-commands', action='store_true')

    tools_parser = subparsers.add_parser('tools', help=t('cmd.tools.help'))
    tools_parser.add_argument('--limit', type=int, default=20)
    tools_parser.add_argument('--query')
    tools_parser.add_argument('--simple-mode', action='store_true')
    tools_parser.add_argument('--no-mcp', action='store_true')
    tools_parser.add_argument('--deny-tool', action='append', default=[])
    tools_parser.add_argument('--deny-prefix', action='append', default=[])

    route_parser = subparsers.add_parser('route', help=t('cmd.route.help'))
    route_parser.add_argument('prompt')
    route_parser.add_argument('--limit', type=int, default=5)

    bootstrap_parser = subparsers.add_parser('bootstrap', help=t('cmd.bootstrap.help'))
    bootstrap_parser.add_argument('prompt')
    bootstrap_parser.add_argument('--limit', type=int, default=5)

    loop_parser = subparsers.add_parser('turn-loop', help=t('cmd.turn_loop.help'))
    loop_parser.add_argument('prompt')
    loop_parser.add_argument('--limit', type=int, default=5)
    loop_parser.add_argument('--max-turns', type=int, default=3)
    loop_parser.add_argument('--structured-output', action='store_true')

    flush_parser = subparsers.add_parser('flush-transcript', help=t('cmd.flush_transcript.help'))
    flush_parser.add_argument('prompt')

    load_session_parser = subparsers.add_parser('load-session', help=t('cmd.load_session.help'))
    load_session_parser.add_argument('session_id')

    remote_parser = subparsers.add_parser('remote-mode', help=t('cmd.remote_mode.help'))
    remote_parser.add_argument('target')
    ssh_parser = subparsers.add_parser('ssh-mode', help=t('cmd.ssh_mode.help'))
    ssh_parser.add_argument('target')
    teleport_parser = subparsers.add_parser('teleport-mode', help=t('cmd.teleport_mode.help'))
    teleport_parser.add_argument('target')
    direct_parser = subparsers.add_parser('direct-connect-mode', help=t('cmd.direct_connect.help'))
    direct_parser.add_argument('target')
    deep_link_parser = subparsers.add_parser('deep-link-mode', help=t('cmd.deep_link.help'))
    deep_link_parser.add_argument('target')

    show_command = subparsers.add_parser('show-command', help=t('cmd.show_command.help'))
    show_command.add_argument('name')
    show_tool = subparsers.add_parser('show-tool', help=t('cmd.show_tool.help'))
    show_tool.add_argument('name')

    exec_command_parser = subparsers.add_parser('exec-command', help=t('cmd.exec_command.help'))
    exec_command_parser.add_argument('name')
    exec_command_parser.add_argument('prompt')

    exec_tool_parser = subparsers.add_parser('exec-tool', help=t('cmd.exec_tool.help'))
    exec_tool_parser.add_argument('name')
    exec_tool_parser.add_argument('payload')
    return parser


def main(argv: list[str] | None = None) -> int:
    # Pre-parse --lang to set locale before building full parser
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument('--lang', choices=['en', 'zh', 'hi', 'es', 'fr'], default=None)
    pre_args, _ = pre_parser.parse_known_args(argv)

    parser = build_parser(lang=pre_args.lang)
    args = parser.parse_args(argv)
    manifest = build_port_manifest()
    if args.command == 'summary':
        print(QueryEnginePort(manifest).render_summary())
        return 0
    if args.command == 'manifest':
        print(manifest.to_markdown())
        return 0
    if args.command == 'parity-audit':
        print(run_parity_audit().to_markdown())
        return 0
    if args.command == 'setup-report':
        print(run_setup().as_markdown())
        return 0
    if args.command == 'command-graph':
        print(build_command_graph().as_markdown())
        return 0
    if args.command == 'tool-pool':
        print(assemble_tool_pool().as_markdown())
        return 0
    if args.command == 'bootstrap-graph':
        print(build_bootstrap_graph().as_markdown())
        return 0
    if args.command == 'subsystems':
        for subsystem in manifest.top_level_modules[: args.limit]:
            print(f'{subsystem.name}\t{subsystem.file_count}\t{subsystem.notes}')
        return 0
    if args.command == 'commands':
        if args.query:
            print(render_command_index(limit=args.limit, query=args.query))
        else:
            commands = get_commands(include_plugin_commands=not args.no_plugin_commands, include_skill_commands=not args.no_skill_commands)
            output_lines = [t('msg.command_entries', count=len(commands)), '']
            output_lines.extend(f'- {module.name} — {module.source_hint}' for module in commands[: args.limit])
            print('\n'.join(output_lines))
        return 0
    if args.command == 'tools':
        if args.query:
            print(render_tool_index(limit=args.limit, query=args.query))
        else:
            permission_context = ToolPermissionContext.from_iterables(args.deny_tool, args.deny_prefix)
            tools = get_tools(simple_mode=args.simple_mode, include_mcp=not args.no_mcp, permission_context=permission_context)
            output_lines = [t('msg.tool_entries', count=len(tools)), '']
            output_lines.extend(f'- {module.name} — {module.source_hint}' for module in tools[: args.limit])
            print('\n'.join(output_lines))
        return 0
    if args.command == 'route':
        matches = PortRuntime().route_prompt(args.prompt, limit=args.limit)
        if not matches:
            print(t('msg.no_matches'))
            return 0
        for match in matches:
            print(f'{match.kind}\t{match.name}\t{match.score}\t{match.source_hint}')
        return 0
    if args.command == 'bootstrap':
        print(PortRuntime().bootstrap_session(args.prompt, limit=args.limit).as_markdown())
        return 0
    if args.command == 'turn-loop':
        results = PortRuntime().run_turn_loop(args.prompt, limit=args.limit, max_turns=args.max_turns, structured_output=args.structured_output)
        for idx, result in enumerate(results, start=1):
            print(t('msg.turn_header', index=idx))
            print(result.output)
            print(f'stop_reason={result.stop_reason}')
        return 0
    if args.command == 'flush-transcript':
        engine = QueryEnginePort.from_workspace()
        engine.submit_message(args.prompt)
        path = engine.persist_session()
        print(path)
        print(t('msg.flushed', flushed=engine.transcript_store.flushed))
        return 0
    if args.command == 'load-session':
        session = load_session(args.session_id)
        print(t('msg.session_info', session_id=session.session_id, count=len(session.messages), input=session.input_tokens, output=session.output_tokens))
        return 0
    if args.command == 'remote-mode':
        print(run_remote_mode(args.target).as_text())
        return 0
    if args.command == 'ssh-mode':
        print(run_ssh_mode(args.target).as_text())
        return 0
    if args.command == 'teleport-mode':
        print(run_teleport_mode(args.target).as_text())
        return 0
    if args.command == 'direct-connect-mode':
        print(run_direct_connect(args.target).as_text())
        return 0
    if args.command == 'deep-link-mode':
        print(run_deep_link(args.target).as_text())
        return 0
    if args.command == 'show-command':
        module = get_command(args.name)
        if module is None:
            print(t('msg.command_not_found', name=args.name))
            return 1
        print('\n'.join([module.name, module.source_hint, module.responsibility]))
        return 0
    if args.command == 'show-tool':
        module = get_tool(args.name)
        if module is None:
            print(t('msg.tool_not_found', name=args.name))
            return 1
        print('\n'.join([module.name, module.source_hint, module.responsibility]))
        return 0
    if args.command == 'exec-command':
        result = execute_command(args.name, args.prompt)
        print(result.message)
        return 0 if result.handled else 1
    if args.command == 'exec-tool':
        result = execute_tool(args.name, args.payload)
        print(result.message)
        return 0 if result.handled else 1
    parser.error(t('msg.unknown_cli_command', command=args.command))
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
