Summary:	CUPS Common Print Dialog Backend
Summary(pl.UTF-8):	Backend CUPS dla CPDB (wspólnych okien dialogowych drukowania)
Name:		cpdb-backend-cups
Version:	1.1.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/OpenPrinting/cpdb-backend-cups/releases
Source0:	https://github.com/OpenPrinting/cpdb-backend-cups/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc57c0072f31f20d851cad93e76f98dc
URL:		https://github.com/OpenPrinting/cpdb-backend-cups
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
# pkgconfig(cpdb-libs-backend)
BuildRequires:	cpdb-libs-devel >= 1.2.0
BuildRequires:	cups-devel >= 1:2.2
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	cpdb-libs >= 1.2.0
Requires:	cups >= 1:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the CUPS Common Print Dialog Backend. This
backend manages and provides information about CUPS and IPP printing
destinations to the printing dialog.

%description -l pl.UTF-8
Ten pakiet zawiera backend CUPS dla CPDB (Common Printing Dialog
Backends - wspólnych backendów okien dialogowych drukowania). Ten
backend zarządza i dostarcza informacje o urządzeniach docelowych
drukowania przez CUPS i IPP.

%prep
%setup -q

%build
%{__aclocal}
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
%doc LICENSE.md README.md
%attr(755,root,root) %{_libdir}/print-backends/cups
%{_datadir}/dbus-1/services/org.openprinting.Backend.CUPS.service
%{_datadir}/print-backends/org.openprinting.Backend.CUPS
