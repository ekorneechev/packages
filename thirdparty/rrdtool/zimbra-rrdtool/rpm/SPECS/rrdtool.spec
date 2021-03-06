Summary:            Zimbra's RRDTool build
Name:               zimbra-rrdtool
Version:            VERSION
Release:            alt1
License:            GPL-2.0
Source:             %{name}-%{version}.tar.gz
BuildRequires:      zimbra-libpng-devel
BuildRequires:      zimbra-libart-devel
BuildRequires:      zimbra-freetype-devel
BuildRequires:      zlib-devel, pkgconfig
BuildRequires:      perl-devel
Requires:           zlib, perl
Requires:           zimbra-rrdtool-libs = %{version}-%{release}
AutoReqProv:        no
URL:                http://oss.oetiker.ch/rrdtool/
Group:              Development/Databases

%description
The Zimbra RRDTool build

%prep
%setup -n rrdtool-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-fPIC -O2 -g"; export CFLAGS; \
PKG_CONFIG_PATH="OZCL/pkgconfig"; export PKG_CONFIG_PATH; \
./configure --prefix=OZC \
  --disable-tcl --disable-ruby --disable-python \
  --with-perl-options="INSTALL_BASE=OZC LIB=OZCL/perl5 \
    LIBS='-LOZCL -lm -lpng -lz -lfreetype' INSTALLSITEMAN3DIR='OZCS/man/man3'"
make

%define perl_archname %(perl -MConfig -e 'print $Config{archname}')
%install
make install DESTDIR=${RPM_BUILD_ROOT}
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/perllocal.pod
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/auto/*/.packlist

%package libs
Summary:            RRDTool Libaries
Requires:           zimbra-libpng-libs, zimbra-base
Requires:           zimbra-libart-libs
Requires:           zimbra-freetype-libs
Requires:           zlib, perl
AutoReqProv:        no
Group:              System/Libraries

%description libs
The zimbra-rrdtool-libs package contains the rrdtool libraries

%package devel
Summary:        RRDTool Development
Requires:       zimbra-rrdtool-libs = %{version}-%{release}
AutoReqProv:        no
Group:          Development/C

%description devel
The zimbra-rrdtool-devel package contains the linking libraries and include files

%files
%defattr(-,root,root)
OZCB
OZCS

%files libs
%defattr(-,root,root)
OZCL/*.so.*
OZCL/perl5

%files devel
%defattr(-,root,root)
OZCI
OZCL/*.a
OZCL/*.la
OZCL/*.so

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

