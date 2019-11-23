#!/usr/bin/env python

from gi.repository import Gtk, Gdk, Pango
import gi
gi.require_version('Gtk', '3.0')


class MyMenuWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="MyMenu", resizable=True, decorated=False, default_width=600)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        entry = Gtk.Entry()
        main_box.pack_start(entry, True, True, 0)

        result_list = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        icon = Gtk.Image(stock='gtk-about', icon_size=Gtk.IconSize.DIALOG)
        icon.set_halign(Gtk.Align.START)
        icon.set_valign(Gtk.Align.CENTER)
        result_list.pack_start(icon, False, False, 0)

        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        info_box.set_valign(Gtk.Align.CENTER)

        title = Gtk.Label('Kitty')
        title.set_halign(Gtk.Align.START)
        title.set_ellipsize(Pango.EllipsizeMode.END)
        info_box.pack_start(title, True, True, 0)

        description = Gtk.Label(
            'A fast, feature full, GPU based terminal emulator'
        )
        description.set_halign(Gtk.Align.START)
        description.set_ellipsize(Pango.EllipsizeMode.END)
        info_box.pack_start(description, True, True, 0)

        result_list.pack_start(info_box, True, True, 0)

        shortcut = Gtk.Label('Alt+1')
        shortcut.set_valign(Gtk.Align.CENTER)
        result_list.pack_start(shortcut, False, False, 0)

        main_box.pack_start(result_list, False, False, 0)

        self.add(main_box)


def quit_if_esc(w, e):
    if e.keyval == Gdk.KEY_Escape:
        Gtk.main_quit()
        return True
    return False


def main():
    css = b'''
        window > box > entry {
            border-radius: 0px;
            box-shadow: none;
            background: inherit;
        }
        window > box > box {
        }
        window > box > box > image {
        }
        window > box > box > box {
        }
        window > box > box > box > label:first-child {
        }
        window > box > box > label {
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
