# Run tests in check section
%bcond_without check

%global goipath         github.com/xlab/handysort
%global commit          fb3537ed64a14615a020f0fe8dc08424233d491f
%global common_description %{expand:
This is a Go package implementing a correct comparison function to
compare alphanumeric strings with respect to their integer parts.}

Version:        0

%gometa

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        Alphanumeric string sorting algorithm implementation in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup

%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Aug 13 2018 Gabe <redhatrises@gmail.com> - 0-0.1.20180813gitfb3537e
- First package for Fedora
