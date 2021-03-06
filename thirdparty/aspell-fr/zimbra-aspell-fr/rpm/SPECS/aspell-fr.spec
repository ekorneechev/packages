Summary:            Zimbra's Aspell French dictionary
Name:               zimbra-aspell-fr
Version:            VERSION
Release:            alt1
License:            GPL-2.0
Patch0:             aspell-fr.patch
Source:             %{name}-%{version}.tar.bz2
BuildRequires:      zimbra-aspell
Requires:           zimbra-aspell
AutoReqProv:        no
URL:                http://aspell.net/
Group: 		    Text tools

%description
The Zimbra Aspell French dictionary

%define debug_package %{nil}

%prep
%setup -n aspell-fr-ADICT
%patch0 -p1

%build
LDFLAGS="-Wl,-rpath,/opt/zimbra/common/lib"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --vars ASPELL=OZCB/aspell \
 WORD_LIST_COMPRESS=OZCB/word-list-compress
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
OZCL/aspell-0.60

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

