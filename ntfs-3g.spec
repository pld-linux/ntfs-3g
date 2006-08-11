%define		_beta	BETA

Summary:	The NTFS driver with read and write support
Summary(pl):	Sterownik do NTFS umożliwiający odczyt i zapis
Name:		ntfs-3g
Version:	20070811
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications/System
Source0:	http://mlf.linux.rulez.org/mlf/ezaz/%{name}-%{version}-%{_beta}.tgz
# Source0-md5:	cf3e7cd55454b9e26e5c3fa749e478bc
Patch0:		%{name}-Makefile.am.diff
URL:		http://www.linux-ntfs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libfuse-devel >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static version of libntfs-3g library

%description static -l pl
Ten pakiet zawiera statyczną wersję bibliotek libntfs-3g.

%prep
%setup -q -n %{name}-%{version}-%{_beta}
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

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ntfs-3g
%{_libdir}/*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
