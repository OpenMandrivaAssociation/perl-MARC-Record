%define module	MARC-Record
%define name	perl-%{module}
%define version 2.0.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp.perl.org/pub/CPAN/modules/by-module/MARC/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/

BuildArch:	noarch

%description
Module for handling MARC records as objects.
The file-handling stuff is in MARC::File::*.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
#chmod 644  $RPM_BUILD_ROOT/%{perl_vendorlib}/MARC/Record.pm
#chmod 644  $RPM_BUILD_ROOT/%{perl_vendorlib}/MARC/Field.pm

%files
%defattr(-,root,root)
%{_bindir}/marcdump
%doc Changes README
%{perl_vendorlib}/MARC
%{_mandir}/*/*


