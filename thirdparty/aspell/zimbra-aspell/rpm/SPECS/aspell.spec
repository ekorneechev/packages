Summary:            Zimbra's Aspell build
Name:               zimbra-aspell
Version:            VERSION
Release:            alt1.zimbra844
License:            LGPL-2.1
Source:             %{name}-%{version}.tar.gz
BuildRequires:      libncurses-devel
Requires:           libncurses, zimbra-aspell-libs = %{version}-%{release}
AutoReqProv:        no
URL:                http://aspell.net/
Group:              Text tools

%description
The Zimbra Aspell build

%prep
%set_verify_elf_method skip
%setup -n aspell-%{version}

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        Aspell Libaries
Requires:       zimbra-spell-base
AutoReqProv:        no
Group:              Development/C

%description libs
The zimbra-aspell-libs package contains the aspell libraries

%package devel
Summary:        Aspell Development
Requires: zimbra-aspell-libs = %{version}-%{release}
AutoReqProv:        no
Group:              Development/C

%description devel
The zimbra-aspell-devel package contains the linking libraries and include files

%files
%defattr(-,root,root)
OZCB
OZCS

%files libs
%defattr(-,root,root)
%dir OZCL/aspell-0.60
OZCL/*.so.*
OZCL/aspell-0.60

%files devel
%defattr(-,root,root)
OZCI
OZCL/*.la
OZCL/*.so

