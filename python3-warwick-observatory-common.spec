Name:           python3-warwick-observatory-common
Version:        2.1.19
Release:        0
License:        GPL3
Summary:        Common backend code for the Warwick La Palma telescopes
Url:            https://github.com/warwick-one-metre/
BuildArch:      noarch
Requires:       python3, python3-Pyro4
Provides:       python36-warwick-observatory-common = 2.1.19

%description
Part of the observatory software for the Warwick one-meter telescope and other La Palma facilities.

warwick-observatory-common holds the common backend code shared by the other utilities.

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog