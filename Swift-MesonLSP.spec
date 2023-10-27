%global debug_package %{nil}
%undefine _auto_set_build_flags

Name:           Swift-MesonLSP
Version:        3.0.20
Release:        0.1
Summary:        Meson language server
ExclusiveArch:  x86_64

License:        GPL-3.0-or-later
Source0:        https://github.com/JCWasmx86/Swift-MesonLSP/archive/refs/tags/v%{version}.tar.gz

Requires:       bash
BuildRequires:  swift-lang
BuildRequires:  clang
BuildRequires:  git

%description
A meson language server

%prep
%setup -q -n Swift-MesonLSP-%{version}

%build
git clone https://github.com/JCWasmx86/Swift-MesonLSP
cd Swift-MesonLSP
git checkout v%{version}
swift build -c release --static-swift-stdlib -Xswiftc -g

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp Swift-MesonLSP/.build/release/Swift-MesonLSP $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/Swift-MesonLSP

%changelog
* Fri Oct 27 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.20-0.1
- Bump to v3.0.20
* Fri Oct 27 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.19-0.1
- Bump to v3.0.19
* Fri Oct 27 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.18-0.1
- Bump to v3.0.18
* Fri Oct 27 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.17-0.1
- Bump to v3.0.17
* Fri Oct 27 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.16-0.1
- Bump to v3.0.16
* Fri Oct 27 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.15-0.1
- Bump to v3.0.15
* Fri Oct 27 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.14-0.1
- Bump to v3.0.14
* Wed Oct 25 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.13-0.1
- Bump to v3.0.13
* Wed Oct 25 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.12-0.1
- Bump to v3.0.12
* Wed Oct 25 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.11-0.1
- Bump to v3.0.11
* Wed Oct 25 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.10-0.1
- Bump to v3.0.10
* Wed Oct 25 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.9-0.1
- Bump to v3.0.9
* Wed Oct 25 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.8-0.1
- Bump to v3.0.8
* Wed Oct 25 2023 JCWasmx86 <JCWasmx86@t-online.de> - 3.0.7-0.1
- Bump to v3.0.7
* Tue Oct 24 2023 FeRD (Frank Dana) <ferdnyc@gmail.com> - 3.0.6-0.1
- Fix versioning
- Use SPDX license tag
- Use %%{version} for easier specfile maintenance

* Tue Oct 24 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.34
- Bump to v3.0.6
* Mon Oct 23 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.33
- Bump to v3.0.5
* Mon Oct 23 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.32
- Bump to v3.0.4
* Mon Oct 23 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.31
- Bump to v3.0.3
* Mon Oct 23 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.30
- Bump to v3.0.2
* Mon Oct 23 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.29
- Bump to v3.0.1
* Mon Oct 23 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.28
- Bump to v3.0.0
* Sun Oct 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.27
- Bump to v2.4.4
* Fri Sep 22 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.26
- Bump to v2.4.3
* Wed Sep 20 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.25
- Bump to v2.4.2
* Mon Sep 11 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.24
- Bump to v2.4.1
* Sat Sep 02 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.23
- Bump to v2.4
* Thu Jul 06 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.22
- Bump to v2.3.15
* Thu Jul 06 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.21
- Bump to v2.3.14
* Thu Jul 06 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.20
- Bump to v2.3.13
* Wed Jul 05 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.19
- Bump to v2.3.12
* Wed Jul 05 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.18
- Bump to v2.3.11
* Wed Jul 05 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.17
- Bump to v2.3.10
* Wed Jul 05 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.16
- Bump to v2.3.9
* Sat Jul 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.15
- Bump to v2.3.8
* Sat Jul 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.14
- Bump to v2.3.7
* Sat Jul 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.13
- Bump to v2.3.6
* Sat Jul 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.12
- Bump to v2.3.5
* Sat Jul 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.11
- Bump to v2.3.4
* Sat Jul 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.10
- Bump to v2.3.3
* Sat Jul 01 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.9
- Bump to v2.3.2
* Fri Jun 16 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.8
- Bump to v2.3.1
* Thu Jun 8 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.7
- Bump to v2.3
* Sat May 13 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.6
- Bump to v2.2
* Fri Apr 21 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.5
- Bump to v2.1
* Sun Apr 2 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.4
- Bump to v2.0
* Sun Apr 2 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.3
- Bump to v1.6
* Sun Apr 2 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.2
- Bump to v1.5.1
* Sat Apr 1 2023 JCWasmx86 <JCWasmx86@t-online.de> - 0.0.1
- First version being packaged
