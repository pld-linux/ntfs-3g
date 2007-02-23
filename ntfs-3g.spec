Summary:	The NTFS driver with read and write support
Summary(pl):	Sterownik do NTFS umożliwiający odczyt i zapis
Name:		ntfs-3g
Version:	1.0
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://www.ntfs-3g.org/%{name}-%{version}.tgz
# Source0-md5:	873a8de662849d129fc7c475ad3f5447
Patch0:		%{name}-ldconfig.patch
URL:		http://www.ntfs-3g.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.6.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The driver to NTFS with read and write support. It is able to
unlimited and fully save file creation and deletion.

%description -l pl
Sterownik do systemu plików NTFS posiadający możliwość zarówno odczytu
jak i zapisu. Umożliwia tworzenie i kasowanie plików nieograniczoną
liczbę razy.

%package devel
Summary:	Header files for libntfs-3g library
Summary(pl):	Pliki nagłówkowe dla biblioteki libntfs-3g
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package includes the header files needed to link software with
libnfts-3g libraries.

%description devel -l pl
Pliki nagłówkowe potrzebne do budowania programów korzystających z
bibliotek libntfs-3g.

%package static
Summary:	Static version of libntfs-3g library
Summary:	Statyczna wersja bibliotek libntfs-3g
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains the static version of libntfs-3g library

%description static -l pl
Ten pakiet zawiera statyczną wersję bibliotek libntfs-3g.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ntfs-3g
%attr(755,root,root) %{_sbindir}/mount.ntfs-3g
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ntfs-3g

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
