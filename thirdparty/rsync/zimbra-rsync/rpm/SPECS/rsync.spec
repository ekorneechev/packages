Summary:            Zimbra's rsync build
Name:               zimbra-rsync
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            GPL-3
Source:             %{name}-%{version}.tar.gz
BuildRequires:      libpopt-devel
Requires:           libpopt, zimbra-base
AutoReqProv:        no
URL:                https://rsync.samba.org
Group:              Networking/File transfer

%description
The Zimbra rsync build

%prep
%setup -n rsync-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC \
  --localstatedir=$(ZIMBRA_HOME)/data/tmp
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
OZCB
OZCS
