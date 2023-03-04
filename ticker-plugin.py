import sublime
import sublime_plugin

class TickerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.set_status(
                        'text', 'I like this.'
        )
            
    def is_visible(self):
        print(self.view.window().active_panel())
        return True 