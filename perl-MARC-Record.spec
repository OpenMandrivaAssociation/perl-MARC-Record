%define module	MARC-Record

Name:		perl-%{module}
Version:	2.0.3
Release:	4
Summary:	%{module} module for perl
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		ftp.perl.org/pub/CPAN/modules/by-module/MARC/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Module for handling MARC records as objects.
The file-handling stuff is in MARC::File::*.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/marcdump
%{perl_vendorlib}/MARC
%{_mandir}/*/*

%changelog
* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.3-1mdv2011.0
+ Revision: 636195
- new version

* Fri May 07 2010 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 2.0.2-1mdv2011.0
+ Revision: 543146
- Update to 2.0.2

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-5mdv2010.0
+ Revision: 430498
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-4mdv2009.0
+ Revision: 257751
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-3mdv2009.0
+ Revision: 245821
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.0.0-1mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 14 2007 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 2.0.0-1mdv2007.0
+ Revision: 120948
- Update to 2.0.0
- MARC::Lint is now in a separate module
- Import perl-MARC-Record

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.38-2mdk
- Fix According to perl Policy
	- Source URL

* Thu May 04 2006 Jerome Soyer <saispo@mandriva.org> 1.38-1mdk
- From Stéphane Téletchéa <steletch@mandriva.org>
- Initial Mandriva release

