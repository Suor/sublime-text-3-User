import sublime, sublime_plugin


class ToggleLayoutCommand(sublime_plugin.WindowCommand):
    def run(self):
        win = self.window

        win.run_command('toggle_tabs')
        win.run_command('toggle_minimap')
        win.run_command('toggle_side_bar')
        if win.num_groups() == 1:
            win.run_command('set_layout', {
                "cols": [0.0, 0.5, 1.0],
                "rows": [0.0, 1.0],
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
            })
        elif win.num_groups() == 2:
            win.run_command('set_layout', {
                "cols": [0.0, 1.0],
                "rows": [0.0, 1.0],
                "cells": [[0, 0, 1, 1]]
            })
