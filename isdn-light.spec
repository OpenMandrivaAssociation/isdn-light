Summary:	Networking with the isdn subsystem, light version
Name:		isdn-light
Version:	0.8
Release:	%mkrel 18
License:	GPL
Group:		System/Kernel and hardware
URL:		http://cvs.mandriva.com
Source:		%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{version}-%{release}-buildroot
Requires:	isdn4k-utils
Conflicts:	isdn4net

%description
This package provides the minimal scripts to do networking with isdn4linux.
It is simple, clean and tiny. Ideal for small configuration.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_sysconfdir}/sysconfig/network-scripts/ifcfg-ippp0

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/isdn/
%config(noreplace) %{_sysconfdir}/isdn/isdnctrl.conf
%config(noreplace) %{_sysconfdir}/isdn/isdn1B.conf
%config(noreplace) %{_sysconfdir}/isdn/isdn2B.conf
%config(noreplace) %{_sysconfdir}/ppp/ioptions
%config(noreplace) %{_sysconfdir}/ppp/ioptions1B
%config(noreplace) %{_sysconfdir}/ppp/ioptions2B
%config(noreplace) %{_sysconfdir}/sysconfig/network-scripts/ifup-ippp
%config(noreplace) %{_sysconfdir}/sysconfig/network-scripts/ifdown-ippp
%doc README


