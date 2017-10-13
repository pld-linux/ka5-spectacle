%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		spectacle

Summary:	Spectacle
Summary(pl.UTF-8):	Spectacle
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c5f3302263ab882be20099a3fc3ea7f7
URL:		http://www.kde.org/
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
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
