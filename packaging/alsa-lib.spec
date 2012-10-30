Name:           alsa-lib
Version:        1.0.25
Release:        1
License:        LGPL-2.0+
Summary:        The Advanced Linux Sound Architecture (ALSA) library
Url:            http://www.alsa-project.org/
Group:          System/Libraries
Source0:        ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.gz

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.

%package -n libasound
Summary:        ALSA Library package for multimedia framework middleware package
Group:          Development/Libraries

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


%build
%configure --disable-static \
    --with-alsa-devdir=/dev/snd \
    --disable-alisp \
    --disable-seq \
    --disable-rawmidi \
    --disable-python \
    --with-gnu-ld \
    --with-pcm-plugins=rate,linear,plug,dmix,dsnoop,asym,mmap,ioplug

make %{?_smp_mflags}

%install
%make_install

rm -f %{buildroot}/%{_bindir}/aserver

%post -n libasound -p /sbin/ldconfig

%postun -n libasound -p /sbin/ldconfig


%files -n libasound
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/alsa-lib/smixer/*.so
%{_datadir}/alsa/*

%files -n libasound-devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal

