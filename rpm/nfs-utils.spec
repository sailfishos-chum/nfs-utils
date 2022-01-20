# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       nfs-utils

# >> macros
# << macros

Summary:    NFS client and server daemons
Version:    2.5.4
Release:    1
Group:      System
License:    GPLv2
URL:        http://linux-nfs.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  nfs-utils.yaml
Requires:   rpcbind
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(libevent_core)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(systemd)

%description

%if "%{?vendor}" == "chum"
PackageName: NFS Utils
PackagerName: nephros
Categories:
 - Network
 - Filesystem
 - System
%endif


%package doc
Summary:    Documentation files for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%package devel
Summary:    Developmemt files for %{name}
Group:      System
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --with-gnu-ld \
    --disable-gss \
    --disable-nfsdcld \
    --disable-nfsdcltrack \
    --with-systemd=%{_unitdir}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_sbindir}/*
/sbin/mount.*
/sbin/umount.*
%{_libdir}/*.so.*
%{_libdir}/libnfsidmap/*.so
%{_unitdir}/*
%{_systemdgeneratordir}/*
%{_sharedstatedir}/nfs
# >> files
# << files

%files doc
%defattr(-,root,root,-)
%{_mandir}/*/*
# >> files doc
# << files doc

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
# >> files devel
# << files devel