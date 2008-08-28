Summary:	The NTFS driver with read and write support
Summary(pl.UTF-8):	Sterownik do NTFS umożliwiający odczyt i zapis
Name:		ntfs-3g
Version:	1.2812
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.ntfs-3g.org/%{name}-%{version}.tgz
# Source0-md5:	b250a8d6603dc8c5411ee50bea444ccb
URL:		http://www.ntfs-3g.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.7.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The driver to NTFS with read and write support. It is able to
unlimited and fully save file creation and deletion.

%description -l pl.UTF-8
Sterownik do systemu plików NTFS posiadający możliwość zarówno odczytu
jak i zapisu. Umożliwia tworzenie i kasowanie plików nieograniczoną
liczbę razy.

%package devel
Summary:	Header files for libntfs-3g library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki libntfs-3g
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package includes the header files needed to link software with
libnfts-3g libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania programów korzystających z
bibliotek libntfs-3g.

%package static
Summary:	Static version of libntfs-3g library
Summary:	Statyczna wersja bibliotek libntfs-3g
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains the static version of libntfs-3g library

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję bibliotek libntfs-3g.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--disable-ldconfig \
	--with-fuse=external

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# mount.ntfs-3g manpage fix
rm $RPM_BUILD_ROOT%{_mandir}/man8/mount.ntfs-3g.8
echo ".so ntfs-3g.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mount.ntfs-3g.8

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ntfs-3g
%attr(755,root,root) %{_bindir}/ntfs-3g.probe
%attr(755,root,root) %{_sbindir}/mount.ntfs-3g
%attr(755,root,root) %{_libdir}/libntfs-3g.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntfs-3g.so.36
%{_mandir}/man8/mount.ntfs-3g.8*
%{_mandir}/man8/ntfs-3g.8*
%{_mandir}/man8/ntfs-3g.probe.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntfs-3g.so
%{_libdir}/libntfs-3g.la
%{_includedir}/ntfs-3g
%{_pkgconfigdir}/libntfs-3g.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libntfs-3g.a
