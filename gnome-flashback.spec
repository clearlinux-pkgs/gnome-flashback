#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-flashback
Version  : 3.42.0
Release  : 25
URL      : https://download.gnome.org/sources/gnome-flashback/3.42/gnome-flashback-3.42.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-flashback/3.42/gnome-flashback-3.42.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-flashback-bin = %{version}-%{release}
Requires: gnome-flashback-data = %{version}-%{release}
Requires: gnome-flashback-lib = %{version}-%{release}
Requires: gnome-flashback-libexec = %{version}-%{release}
Requires: gnome-flashback-license = %{version}-%{release}
Requires: gnome-flashback-locales = %{version}-%{release}
Requires: gnome-flashback-services = %{version}-%{release}
Requires: gnome-screensaver
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : gnome-screensaver
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gdm)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-bluetooth-1.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libgnome-panel)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb-randr)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xkeyboard-config)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xxf86vm)

%description


%package bin
Summary: bin components for the gnome-flashback package.
Group: Binaries
Requires: gnome-flashback-data = %{version}-%{release}
Requires: gnome-flashback-libexec = %{version}-%{release}
Requires: gnome-flashback-license = %{version}-%{release}
Requires: gnome-flashback-services = %{version}-%{release}

%description bin
bin components for the gnome-flashback package.


%package data
Summary: data components for the gnome-flashback package.
Group: Data

%description data
data components for the gnome-flashback package.


%package lib
Summary: lib components for the gnome-flashback package.
Group: Libraries
Requires: gnome-flashback-data = %{version}-%{release}
Requires: gnome-flashback-libexec = %{version}-%{release}
Requires: gnome-flashback-license = %{version}-%{release}

%description lib
lib components for the gnome-flashback package.


%package libexec
Summary: libexec components for the gnome-flashback package.
Group: Default
Requires: gnome-flashback-license = %{version}-%{release}

%description libexec
libexec components for the gnome-flashback package.


%package license
Summary: license components for the gnome-flashback package.
Group: Default

%description license
license components for the gnome-flashback package.


%package locales
Summary: locales components for the gnome-flashback package.
Group: Default

%description locales
locales components for the gnome-flashback package.


%package services
Summary: services components for the gnome-flashback package.
Group: Systemd services

%description services
services components for the gnome-flashback package.


%prep
%setup -q -n gnome-flashback-3.42.0
cd %{_builddir}/gnome-flashback-3.42.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635960248
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1635960248
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-flashback
cp %{_builddir}/gnome-flashback-3.42.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-flashback/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
%find_lang gnome-flashback
## install_append content
mv %{buildroot}/etc/xdg %{buildroot}/usr/share/. && rmdir %{buildroot}/etc

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-flashback

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-flashback.desktop
/usr/share/desktop-directories/X-GNOME-Flashback-Settings-System.directory
/usr/share/desktop-directories/X-GNOME-Flashback-Settings.directory
/usr/share/glib-2.0/schemas/00_gnome-flashback.gschema.override
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.background.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.desktop.icons.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-flashback.system-indicators.input-sources.gschema.xml
/usr/share/gnome-panel/layouts/gnome-flashback.layout
/usr/share/gnome-session/sessions/gnome-flashback-metacity.session
/usr/share/xdg/autostart/gnome-flashback-clipboard.desktop
/usr/share/xdg/autostart/gnome-flashback-nm-applet.desktop
/usr/share/xdg/menus/gnome-flashback-applications.menu
/usr/share/xsessions/gnome-flashback-metacity.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-panel/modules/system_indicators.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-flashback-clipboard
/usr/libexec/gnome-flashback-metacity

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-flashback/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gnome-flashback.service
/usr/lib/systemd/user/gnome-flashback.target
/usr/lib/systemd/user/gnome-session@gnome-flashback-metacity.target.d/session.conf

%files locales -f gnome-flashback.lang
%defattr(-,root,root,-)

