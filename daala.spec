%global commit0 28de40bfcd84e7df3fbd64de7b89dd7fd889bb27
%global date 20161216
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       daala
Version:    0
Release:    4%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:    Daala video compression
License:    BSD
URL:        http://xiph.org/daala/

Source0:    https://git.xiph.org/?p=%{name}.git;a=snapshot;h=%{commit0};sf=tgz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(check) >= 0.9.8
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg) >= 1.3
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  wxGTK-devel

%description
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package    libs
Summary:    Daala video codec libraries

%description libs
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

%package    devel
Summary:    Development files for the Daala video codec libraries
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package    tools
Summary:    Daala video codec tools

%description tools
A new video compression technology. The goal of the project is to provide a
video format that's free to implement, use and distribute, and a reference
implementation with technical performance superior to H.265.

The %{name}-tools package contains a test player and encoder plus programs for
testing %{name} support in your applications.

%prep
%setup -q -n %{name}-%{shortcommit0}

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-analyzer \
    --enable-float-pvq

%make_build
%make_build tools

%install
%make_install
find %{buildroot} -name "*.la" -delete

# Install tools (list from tools_TARGETS in Makefile.am)
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p \
    tools/png2y4m \
    tools/y4m2png \
    tools/dump_psnrhvs \
    tools/block_size_analysis \
    tools/to_monochrome \
    tools/downsample \
    tools/upsample \
    tools/divu_const \
    tools/trans \
    tools/trans2d \
    tools/trans_gain \
    tools/gen_cdf \
    tools/gen_sqrt_tbl \
    tools/compute_basis \
    tools/compute_haar_basis \
    tools/cos_search \
    tools/gen_laplace_tables \
    tools/daalainfo \
    tools/dump_ssim \
    tools/dump_fastssim \
    tools/bjontegaard \
    tools/yuvjpeg \
    tools/jpegyuv \
    tools/yuv2yuv4mpeg \
    tools/dump_psnr \
    tools/vq_train \
    tools/draw_zigzags \
    tools/dump_msssim \
    tools/y4m2yuv \
    %{buildroot}%{_bindir}/

# Let rpm pick up the docs in the files section
rm -fr %{buildroot}/%{_docdir}

# Install man pages
mkdir -p %{buildroot}/%{_mandir}
cp -fr doc/man/man3/ %{buildroot}/%{_mandir}
rm -f %{buildroot}/%{_mandir}/man3/_*_include_daala_.3

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files libs
%license COPYING
%doc AUTHORS
%{_libdir}/*.so.*

%files devel
%doc doc/html
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/
%{_mandir}/man3/*

%files tools
%{_bindir}/*

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20161216git28de40b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Simone Caronni <negativo17@gmail.com> - 0-3.20161216git28de40b
- Update to latest snapshot.
- Add docs and enable building of tools.

* Fri Nov 25 2016 Simone Caronni <negativo17@gmail.com> - 0-2.20161117git4eddbab
- Update to latest snapshot.
- Use make_build macro, license macro.

* Fri Nov 18 2016 Simone Caronni <negativo17@gmail.com> - 0-1.20161114git4403315
- First build.

