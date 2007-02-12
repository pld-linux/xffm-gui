Summary:	GUI library for the xffm applications
Summary(pl.UTF-8):   Biblioteka GUI dla aplikacji xffm
Name:		xffm-gui
Version:	4.5.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xffm/%{name}-%{version}.tar.gz
# Source0-md5:	9a06be7c55896949d42587078643ab69
URL:		http://xffm.sourceforge.net/xffm-gui.html
Patch0:		%{name}-asneeded.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxffm-devel >= 4.5.0
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xffm-gui is the basic GUI library used by xffm applications.

%description -l pl.UTF-8
Xffm-gui jest podstawową biblioteką GUI używaną przez aplikacje xffm.

%package devel
Summary:	Header files for xffm-gui library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki xffm-gui
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.6.0
Requires:	libxffm-devel >= 4.5.0

%description devel
Header files for xffm-gui library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xffm-gui.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/{xfce4,xffm}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libxffm_deskview.so.*.*.*
%attr(755,root,root) %{_libdir}/libxffm_gridview.so.*.*.*
%attr(755,root,root) %{_libdir}/libxffm_treeview.so.*.*.*
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxffm_deskview.so
%attr(755,root,root) %{_libdir}/libxffm_gridview.so
%attr(755,root,root) %{_libdir}/libxffm_treeview.so
%{_libdir}/libxffm_deskview.la
%{_libdir}/libxffm_gridview.la
%{_libdir}/libxffm_treeview.la
%{_includedir}/xffm/*.h
%{_pkgconfigdir}/xffm-gui.pc
