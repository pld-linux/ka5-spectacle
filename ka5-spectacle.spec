#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.1
%define		qtver		5.15.2
%define		kaname		spectacle

Summary:	Spectacle
Summary(pl.UTF-8):	Spectacle
Name:		ka5-%{kaname}
Version:	22.08.1
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d7bafa2691ee8e51bd7cac5754da3d95
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
BuildRequires:	kf5-kwayland-devel
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.29.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.29.0
BuildRequires:	kf5-kxmlgui-devel >= 5.29.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= 5.6.0
BuildRequires:	shared-mime-info
BuildRequires:	xcb-util-cursor-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spectacle is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description -l pl.UTF-8
Spectacle to prosta aplikacja do robienia zrzutów ekranu. Potrafi
przechwytywać obraz całego pulpitu lub tylko pojedynczego okna.
Obrazy mogą być następnie zapisane w wielu formatach.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spectacle
%{_desktopdir}/org.kde.spectacle.desktop
%{_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_datadir}/knotifications5/spectacle.notifyrc
%{_datadir}/metainfo/org.kde.spectacle.appdata.xml
%attr(755,root,root) %{_libdir}/kconf_update_bin/spectacle-migrate-shortcuts
%attr(755,root,root) %{_libdir}/kconf_update_bin/spectacle-migrate-rememberregion
%{_datadir}/kconf_update/spectacle_rememberregion.upd
%attr(755,root,root) %{_datadir}/kconf_update/50-clipboard_settings_change.py
%{_datadir}/kconf_update/spectacle_clipboard.upd
%{_datadir}/kconf_update/spectacle_shortcuts.upd
%dir %{_datadir}/kglobalaccel
%{_datadir}/kglobalaccel/org.kde.spectacle.desktop
%{_datadir}/qlogging-categories5/spectacle.categories
%{_datadir}/kconf_update/spectacle_newConfig.upd
%{systemduserunitdir}/app-org.kde.spectacle.service
%{_mandir}/ca/man1/spectacle.1*
%{_mandir}/de/man1/spectacle.1*
%{_mandir}/es/man1/spectacle.1*
%{_mandir}/it/man1/spectacle.1*
%{_mandir}/man1/spectacle.1*
%{_mandir}/nl/man1/spectacle.1*
%{_mandir}/sv/man1/spectacle.1*
%{_mandir}/uk/man1/spectacle.1*
%{_iconsdir}/hicolor/scalable/apps/spectacle.svg
