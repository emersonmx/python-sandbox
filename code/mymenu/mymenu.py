#!/usr/bin/env python

from gi.repository import Gtk, Gdk, Pango
import gi
gi.require_version('Gtk', '3.0')


class ResultItem(Gtk.ListBoxRow):
    def __init__(self):
        super().__init__()

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.icon = Gtk.Image(stock='gtk-missing-image', icon_size=Gtk.IconSize.DIALOG)
        self.icon.set_halign(Gtk.Align.START)
        self.icon.set_valign(Gtk.Align.CENTER)
        box.pack_start(self.icon, False, False, 0)

        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        info_box.set_valign(Gtk.Align.CENTER)

        self.title = Gtk.Label('Title')
        self.title.set_halign(Gtk.Align.START)
        self.title.set_ellipsize(Pango.EllipsizeMode.END)
        info_box.pack_start(self.title, True, True, 0)

        self.description = Gtk.Label('The program description')
        self.description.set_halign(Gtk.Align.START)
        self.description.set_ellipsize(Pango.EllipsizeMode.END)
        info_box.pack_start(self.description, True, True, 0)

        box.pack_start(info_box, True, True, 0)

        shortcut = Gtk.Label('Shortcut')
        shortcut.set_valign(Gtk.Align.CENTER)
        box.pack_start(shortcut, False, False, 0)

        self.add(box)


class MyMenuWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="MyMenu", resizable=True, decorated=False, default_width=600)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        entry = Gtk.Entry()
        main_box.pack_start(entry, True, True, 0)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        listbox.add(ResultItem())
        listbox.add(ResultItem())
        listbox.add(ResultItem())
        listbox.add(ResultItem())

        main_box.pack_start(listbox, False, False, 0)

        self.add(main_box)


def quit_if_esc(w, e):
    if e.keyval == Gdk.KEY_Escape:
        Gtk.main_quit()
        return True
    return False


def main():
    css = b'''
        * {
            border-radius: 0px;
            box-shadow: none;
        }
    '''

    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    window = MyMenuWindow()
    window.connect('key_press_event', quit_if_esc)
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
