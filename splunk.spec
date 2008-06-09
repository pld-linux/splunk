# TODO
# - everything
%define		subver	37025
Summary:	Splunk is IT Search
Name:		splunk
Version:	3.2.4
Release:	0.1
License:	2005-2008 Splunk Inc
Group:		Applications
Source0:	http://download.splunk.com/releases/3.2.4/linux/%{name}-%{version}-%{subver}-Linux-i686.tgz
# Source0-md5:	fd7beed52a2d6047cf781e75f49fd1f5
NoSource:	0
Source1:	http://download.splunk.com/releases/3.2.4/linux/%{name}-%{version}-%{subver}-Linux-x86_64.tgz
# Source1-md5:	ad8a078b8a5a45ff5efa4559d7a45a09
NoSource:	1
URL:		http://www.splunk.com/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Search and navigate IT data

%prep
%ifarch %{ix86}
%setup -q -T -n %{name} -b0
%endif
%ifarch %{x8664}
%setup -q -T -n %{name} -b1
%endif

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
