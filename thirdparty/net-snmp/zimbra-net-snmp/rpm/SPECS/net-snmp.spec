Summary:            Zimbra's NetSNMP build
Name:               zimbra-net-snmp
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            BSD
Source:             %{name}-%{version}.tar.gz
Patch0:		    net-snmp-%{version}-alt.patch
BuildRequires:      zimbra-openssl-devel
BuildRequires:      libnl-devel librpm-devel libsensors3-devel libwrap-devel pdksh perl-devel python-module-setuptools perl-Tk perl-Term-ReadLine-Gnu perl-libnet perl-XML-Simple perl-podlators chrpath
Requires:           perl
Requires:           zimbra-net-snmp-libs = %{version}-%{release}
AutoReqProv:        no
URL:                http://www.net-snmp.org/
Group:              System/Servers

%description
The Zimbra NetSNMP build

%prep
%setup -n net-snmp-%{version}
%set_verify_elf_method skip
%patch0 -p1

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
## https://sourceforge.net/p/net-snmp/bugs/2951/#9d6d
sed -i s/"define HAVE_LIBRPM 1"/""/g configure; \
./configure --prefix=OZC \
  --with-default-snmp-version=3 --with-sys-contact="admin" \
  --with-sys-location="unknown" --with-logfile="/opt/zimbra/log/snmpd.log" \
  --with-openssl=OZC \
  --disable-embedded-perl \
  --with-perl-modules="INSTALL_BASE=OZC LIB=OZCL/perl5 INSTALLSITEMAN3DIR=OZCS/man/man3" \
  --with-persistent-directory="/opt/zimbra/data/snmp/persist" \
  --localstatedir="/opt/zimbra/data/snmp/state"
make

%define perl_archname %(perl -MConfig -e 'print $Config{archname}')
%install
make install DESTDIR=${RPM_BUILD_ROOT}
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/perllocal.pod
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/auto/*/*/.packlist

%package libs
Summary:            NetSNMP Libaries
Requires:           zimbra-openssl-libs, zimbra-snmp-base
AutoReqProv:        no
Group: System/Libraries

%description libs
The zimbra-net-snmp-libs package contains the net-snmp libraries

%package devel
Summary:        NetSNMP Development
Requires:       zimbra-net-snmp-libs = %{version}-%{release}
AutoReqProv:        no
Group: Development/C

%description devel
The zimbra-net-snmp-devel package contains the linking libraries and include files

%files
%defattr(-,root,root)
OZCB
OZCS
%exclude OZC/sbin

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
