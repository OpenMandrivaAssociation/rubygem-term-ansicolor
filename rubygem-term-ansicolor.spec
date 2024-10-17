# Generated from term-ansicolor-1.0.7.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	term-ansicolor

Summary:	Ruby library that colors strings using ANSI escape sequences
Name:		rubygem-%{rbname}

Version:	1.0.7
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://flori.github.com/term-ansicolor
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Ruby library that colors strings using ANSI escape sequences.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(examples|test)'

%install
%gem_install

%files
%{_bindir}/cdiff
%{_bindir}/decolor
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/cdiff
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/decolor
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/term
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*.rb


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.7-2
+ Revision: 774533
- regenerate spec with gem2rpm5
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.7-1
+ Revision: 766993
- version update 1.0.7

* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 584361
- import rubygem-term-ansicolor

