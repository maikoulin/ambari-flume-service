Name: 		flume		
Version:        1.9.0	
Release:	1%{?dist}
Summary:	ambari plugin flume rpm	

Group:		Applications/System	
License:	GPL	
URL:		https://flume.apache.org/
BuildArch:      noarch
Source0:	apache-%{name}-%{version}-bin.tar.gz

%define         userpath /usr/hdp/current/flume-server
Prefix:         %{userpath}

%description
ambari plugin flume 

%prep
%setup -c

%install
install -d $RPM_BUILD_ROOT/%{userpath}
cp -a apache-%{name}-%{version}-bin/* $RPM_BUILD_ROOT/%{userpath}
exit 0


%files
%defattr(-,root,root)
%{userpath}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%changelog

