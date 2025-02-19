"""
Removes a group
"""

from rich import print
from d4v1d.utils import io
from d4v1d.platforms.platform.cmd import Command, CLISessionState
from typing import *

class RemoveGroup(Command):
    """
    Removes a group
    """
    
    def __init__(self):
        """
        Initializes the command.
        """
        super().__init__('add group', description='Remove a group from the currently selected platform.')

    def available(self, state: CLISessionState) -> bool:
        """
        Can this command be used right now?
        """
        return bool(state.platform)

    def execute(self, args: List[str], state: CLISessionState) -> None:
        """
        Executes the command.
        """
        if not state.platform:
            io.e('No platform selected. Use [bold]use[/bold] to select a platform.')
            return
        if not args:
            io.e(f'Missing group name. [bold]Usage:[/bold] rm group <group name>')
            return
        if args[0] not in state.platform.groups:
            io.e(f'Group [bold]{args[0]}[/bold] doesn\'t exist.')
            return
        state.platform.rm_group(args[0])
        print(f'[green]Successfully removed group [bold]{args[0]}[/bold] from platform [bold]{state.platform.name}[/bold].[/green]')