Summary:            Zimbra's tcmalloc build
Name:               zimbra-tcmalloc
Version:            VERSION
Release:            alt1
License:            BSD
Source:             %{name}-%{version}.tar.gz
URL:                https://github.com/gperftools/gperftools
Group: 		    Development/Other

%description
The Zimbra tcmalloc build

%prep
%setup -n gperftools-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC --enable-minimal \
  --enable-static=no --mandir="OZCS/man"
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        tcmalloc Libaries
Requires:       zimbra-base
AutoReqProv:        no
Group: Development/Other

%description libs
The zimbra-tcmalloc-libs package contains the tcmalloc libraries

%package devel
Summary:        tcmalloc Development
Requires: zimbra-tcmalloc-libs = %{version}-%{release}
AutoReqProv:        no
Group: Development/Other

%description devel
The zimbra-tcmalloc-devel package contains the linking libraries and include files

%files libs
%defattr(-,root,root)
OZCL/*.so.*
OZCL/*.so
%exclude OZCS

%files devel
%defattr(-,root,root)
OZCI
OZCL/*.la
OZCL/pkgconfig

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

