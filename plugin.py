import sublime_plugin


class summaryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        summa = 0
        last = None
        for region in selection:
            last = region
            region_text = self.view.substr(region)
            if region_text:
                print(region_text)
                for number in region_text.split():
                    summa += float(number)

            self.view.replace(edit, region, '')

        if summa.is_integer():
            summa = int(summa)

        self.view.replace(edit, last, str(summa))
