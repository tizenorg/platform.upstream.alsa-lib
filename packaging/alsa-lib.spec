Name:           alsa-lib
Version:        1.0.28
Release:        1
License:        LGPL-2.0+
Summary:        The Advanced Linux Sound Architecture (ALSA) library
Url:            http://www.alsa-project.org/
Group:          System/Audio
Source0:        ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
Source1001: 	alsa-lib.manifest

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.

%package -n libasound
Summary:        ALSA Library package for multimedia framework middleware package
Group:          System/Audio

%description -n libasound
ALSA Library package for multimedia framework middleware package

%package -n libasound-devel
Summary:        ALSA Library package for multimedia framework middleware package
Group:          Development/Libraries
Requires:       libasound

%description -n libasound-devel
ALSA Library package for multimedia framework middleware package

%prep
%setup -q
cp %{SOURCE1001} .


%build
%configure --disable-static \
    --with-alsa-devdir=/dev/snd \
    --disable-alisp \
    --disable-python \
    --with-gnu-ld \
    --with-pcm-plugins=rate,linear,plug,dmix,dsnoop,asym,mmap,ioplug,empty,hooks,route,multi,softvol,file,iec958,null,shm

make %{?_smp_mflags}

%install
%make_install

rm -f %{buildroot}/%{_bindir}/aserver

%post -n libasound -p /sbin/ldconfig

%postun -n libasound -p /sbin/ldconfig


%files -n libasound
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/lib*.so.*
%{_libdir}/alsa-lib/smixer/*.so
%{_datadir}/alsa/*

%files -n libasound-devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal

