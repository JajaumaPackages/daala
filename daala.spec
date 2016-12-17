%global commit0 4eddbab067fa434e2d3d96eb5c872ec8a2064468
%global date 20161117
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       daala
Version:    0
Release:    2%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:    Daala video compression
License:    BSD
URL:        http://xiph.org/daala/

Source0:    https://git.xiph.org/?p=%{name}.git;a=snapshot;h=%{commit0};sf=tgz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
# Not yet enabled in the docs makefile:
# BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(check) >= 0.9.8
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg) >= 1.3
BuildRequires:  pkgconfig(sdl2)
# Required for examples:
# BuildRequires:  wxGTK-devel

%description
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package libs
Summary:    Daala video codec libraries

%description libs
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package devel
Summary:    Development files for the Daala video codec libraries
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -q -n %{name}-%{shortcommit0}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

# Let rpm pick up the docs in the files section
rm -fr %{buildroot}/%{_datadir}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files libs
%license COPYING
%doc AUTHORS
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/

%changelog
* Fri Nov 25 2016 Simone Caronni <negativo17@gmail.com> - 0-2.20161117git4eddbab
- Update to latest snapshot.
- Use make_build macro, license macro.

* Fri Nov 18 2016 Simone Caronni <negativo17@gmail.com> - 0-1.20161114git4403315
- First build.

