%global rootpath %{_datadir}/omv

Name:     omv-cli
Version:  0.1.20260208
Release:  1
Summary:  OpenMandriva CLI
License:  -
URL:      https://git.houseof.software/OpenMandriva/Software/cli

BuildArch:  noarch

Source0:  %{name}-%{version}.tar.zst

Requires:  hos-cli

Requires:  bash
Requires:  bubblewrap
Requires:  car
Requires:  curl
Requires:  rpm-build

Recommends:  pv

%description
OpenMandriva's scripts for tasks such as building RPM packages.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}/%{_bindir} \
         %{buildroot}/%{rootpath}

cp %{name} %{buildroot}/%{_bindir}/
cp *.sh %{buildroot}/%{rootpath}/

%files
%{_bindir}/%{name}
%{rootpath}/*
