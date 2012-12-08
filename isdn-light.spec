Summary:	Networking with the isdn subsystem, light version
Name:		isdn-light
Version:	0.8
Release:	%mkrel 25
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8-23mdv2011.0
+ Revision: 665526
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-22mdv2011.0
+ Revision: 605985
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-21mdv2010.1
+ Revision: 520134
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8-20mdv2010.0
+ Revision: 425389
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.8-19mdv2009.1
+ Revision: 351261
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.8-18mdv2009.0
+ Revision: 267925
+ rebuild (emptylog)

* Tue Aug 05 2008 Olivier Blin <oblin@mandriva.com> 0.8-17mdv2009.0
+ Revision: 263852
- do not provide default ifcfg-ippp0, it is already written by config
  tools and the installation of this package should not make an
  unconfigured connection started at boot

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8-16mdv2009.0
+ Revision: 234831
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix URL

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 0.8-14mdv2008.1
+ Revision: 134099
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.8-13mdv2008.1
+ Revision: 127184
- kill re-definition of %%buildroot on Pixel's request


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8-13mdv2007.0
+ Revision: 123900
- Import isdn-light

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8-12mdv2007.1
- use the mrel macro

