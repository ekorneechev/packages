Summary:            Zimbra's Aspell Spanish dictionary
Name:               zimbra-aspell-es
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            GPL-2.0
Source:             %{name}-%{version}.tar.bz2
BuildRequires:      zimbra-aspell
Requires:           zimbra-aspell
AutoReqProv:        no
URL:                http://aspell.net/
Group: 		    Text tools

%description
The Zimbra Aspell Spanish dictionary

%define debug_package %{nil}

%prep
%setup -n aspell6-es-ADICT

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --vars ASPELL=OZCB/aspell \
  PREZIP=OZCB/prezip-bin
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
OZCL/aspell-0.60

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

