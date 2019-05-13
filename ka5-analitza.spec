%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		analitza
Summary:	Analitza
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	63157337ca7a9ae68dd0aa44365c203b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The analitza library will let you add mathematical features to your
program.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build install

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libAnalitza.so.8
%attr(755,root,root) %{_libdir}/libAnalitza.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAnalitzaGui.so.8
%attr(755,root,root) %{_libdir}/libAnalitzaGui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAnalitzaPlot.so.8
%attr(755,root,root) %{_libdir}/libAnalitzaPlot.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAnalitzaWidgets.so.8
%attr(755,root,root) %{_libdir}/libAnalitzaWidgets.so.*.*.*
%dir %{_libdir}/qt5/qml/org/kde/analitza
%{_libdir}/qt5/qml/org/kde/analitza/Graph2D.qml
%{_libdir}/qt5/qml/org/kde/analitza/Graph3D.qml
%{_libdir}/qt5/qml/org/kde/analitza/libanalitzadeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/analitza/qmldir
%dir %{_datadir}/libanalitza
%dir %{_datadir}/libanalitza/plots
%{_datadir}/libanalitza/plots/3Ds.plots
%{_datadir}/libanalitza/plots/basic_curves.plots
%{_datadir}/libanalitza/plots/conics.plots
%{_datadir}/libanalitza/plots/polar.plots

%files devel
%defattr(644,root,root,755)
%{_includedir}/Analitza5
%{_libdir}/cmake/Analitza5
%attr(755,root,root) %{_libdir}/libAnalitza.so
%attr(755,root,root) %{_libdir}/libAnalitzaGui.so
%attr(755,root,root) %{_libdir}/libAnalitzaPlot.so
%attr(755,root,root) %{_libdir}/libAnalitzaWidgets.so
