#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-flashback
Version  : 3.24.0
Release  : 3
URL      : http://ftp.acc.umu.se/pub/gnome/sources/gnome-flashback/3.24/gnome-flashback-3.24.0.tar.xz
Source0  : http://ftp.acc.umu.se/pub/gnome/sources/gnome-flashback/3.24/gnome-flashback-3.24.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-flashback-bin
Requires: gnome-flashback-data
Requires: gnome-flashback-locales
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-bluetooth-1.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xkeyboard-config)
BuildRequires : pkgconfig(xrandr)

%description


%package bin
Summary: bin components for the gnome-flashback package.
Group: Binaries
Requires: gnome-flashback-data

%description bin
bin components for the gnome-flashback package.


%package data
Summary: data components for the gnome-flashback package.
Group: Data

%description data
data components for the gnome-flashback package.


%package locales
Summary: locales components for the gnome-flashback package.
Group: Default

%description locales
locales components for the gnome-flashback package.


%prep
%setup -q -n gnome-flashback-3.24.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492794290
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492794290
rm -rf %{buildroot}
%make_install
%find_lang gnome-flashback
## make_install_append content
mv %{buildroot}/etc/xdg %{buildroot}/usr/share/. && rmdir %{buildroot}/etc
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-flashback
/usr/libexec/gnome-flashback-compiz
/usr/libexec/gnome-flashback-metacity

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-flashback-init.desktop
/usr/share/applications/gnome-flashback.desktop
/usr/share/desktop-directories/X-GNOME-Flashback-Settings-System.directory
/usr/share/desktop-directories/X-GNOME-Flashback-Settings.directory
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.desktop-background.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.input-sources.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.workarounds.gschema.xml
/usr/share/gnome-session/sessions/gnome-flashback-compiz.session
/usr/share/gnome-session/sessions/gnome-flashback-metacity.session
/usr/share/xdg/autostart/gnome-flashback-nm-applet.desktop
/usr/share/xdg/autostart/gnome-flashback-screensaver.desktop
/usr/share/xdg/menus/gnome-flashback-applications.menu
/usr/share/xsessions/gnome-flashback-compiz.desktop
/usr/share/xsessions/gnome-flashback-metacity.desktop

%files locales -f gnome-flashback.lang
%defattr(-,root,root,-)
