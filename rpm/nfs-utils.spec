# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       nfs-utils

# >> macros
# << macros

Summary:    NFS client and server daemons
Version:    2.6.3
Release:    0
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
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
%{summary}.

%if "%{?vendor}" == "chum"
Note that in order to use NFS, you need a kernel that supports it.  
Some SailfishOS devices do, some do not. The Gemini for example does, the XPeria 10III does not.

PackageName: NFS Utils
PackagerName: nephros
Categories:
 - Network
 - Filesystem
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/nfs-utils
Url:
  Help: https://wiki.linux-nfs.org/wiki/index.php/Nfsv4_configuration
  Bugtracker: https://bugzilla.linux-nfs.org
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

# >> macros2
# 4.x has a macro defined, 3.4 uses /usr/lib/systemd, lower uses /lib/systemd
%if %{sailfishos_version} <= 30400
%if %{undefined _systemdgeneratordir}
%define _systemdgeneratordir %{_unitdir}/../system-generators
%endif
%endif
# << macros2

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
sed -i -e "s@udev_rulesdir = /usr/lib/udev/rules.d/@udev_rulesdir = %{_udevrulesdir}@" tools/nfsrahead/Makefile.am
./autogen.sh
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
%{_prefix}/%{_udevrulesdir}/60-nfs.rules
%{_libexecdir}/nfsrahead
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
