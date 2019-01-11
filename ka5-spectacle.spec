%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		spectacle

Summary:	Spectacle
Summary(pl.UTF-8):	Spectacle
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	733a4ef4ed4d355e5cb7a65c3af61f48
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel >= 5.6.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.29.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.29.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.29.0
BuildRequires:	kf5-kdeclarative-devel >= 5.29.0
BuildRequires:	kf5-kdoctools-devel >= 5.29.0
BuildRequires:	kf5-ki18n-devel >= 5.29.0
BuildRequires:	kf5-kio-devel >= 5.29.0
BuildRequires:	kf5-knewstuff-devel >= 5.29.0
BuildRequires:	kf5-knotifications-devel >= 5.29.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.29.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.29.0
BuildRequires:	kf5-kxmlgui-devel >= 5.29.0
BuildRequires:	qt5-build >= 5.6.0
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spectacle is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description -l pl.UTF-8
Spectacle to prosta aplikacja do robienia zrzutów ekranu. Potrafi
przechwytywać obraz całego pulpitu lub tylko pojedynczego okna. Obrazy
mogą być następnie zapisane w wielu formatach.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/spectacle.categories
%attr(755,root,root) %{_bindir}/spectacle
%{_desktopdir}/org.kde.spectacle.desktop
%{_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_iconsdir}/hicolor/16x16/apps/spectacle.png
%{_iconsdir}/hicolor/22x22/apps/spectacle.png
%{_iconsdir}/hicolor/32x32/apps/spectacle.png
%{_iconsdir}/hicolor/48x48/apps/spectacle.png
%{_iconsdir}/hicolor/scalable/apps/spectacle.svgz
%{_datadir}/khotkeys/spectacle.khotkeys
%{_datadir}/knotifications5/spectacle.notifyrc
%{_datadir}/metainfo/org.kde.spectacle.appdata.xml
