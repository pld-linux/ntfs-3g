Summary:	The NTFS driver with read and write support
Summary(pl):	Sterownik do NTFS umo¿liwiaj±cy odczyt i zapis
Summary(pt_BR):	Network Time Protocol versão 4
Name:		ntfs-3g
Version:	20070714
Release:	1beta
License:	distributable
Group:		Applications/System
Source0:	http://mlf.linux.rulez.org/mlf/ezaz/%{name}-%{version}-BETA.tgz
Patch0:		%{name}-Makefile.am.diff
# Source0-md5:	0f8fabe87cf54f409b57c6283f0c0c3d
URL:		http://www.linux-ntfs.org/
BuildRequires:	libfuse-devel >= 2.5.0
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The driver to NTFS with read and write support. It is able to unlimited and 
fully save file creation and deletion.

%description -l pl
Sterownik do systemu plików NTFS posi±daj±cy mo¿liwo¶æ zarówno odczytu jak
i zapisu. Umo¿liwia tworzenie i kasowanie plików nieograniczon± liczbê razy.

%package devel
Summary:	Header files for libntfs-3g library
Summary(pl):	Pliki nag³ówkowe dla biblioteki libntfs-3g
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package includes the header files needed to link software with
libnfts-3g libraries.

%description devel -l pl
Pliki nag³ówkowe potrzebne do budowania programów korzystaj±cych z
bibliotek libntfs-3g.

%package static
Summary:	Static version of libntfs-3g library
Summary:	Statyczna wersja bibliotek libntfs-3g
Group: 		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static version of libntfs-3g library

%description static -l pl
Ten pakiet zawiera statyczn± wersjê bibliotek libntfs-3g.

%prep
%setup -q -n %{name}-%{version}-BETA
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ntfs
%{_libdir}/*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
