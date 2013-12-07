# revision 21912
# category Package
# catalog-ctan /info/translations/fancyhdr/it
# catalog-date 2011-04-01 11:10:52 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-fancyhdr-it
Version:	20110401
Release:	5
Summary:	Italian translation of fancyhdr documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/fancyhdr/it
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr-it.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr-it.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The translation is of documentation provided with the fancyhdr
package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/fancyhdr-it/Makefile
%doc %{_texmfdistdir}/doc/latex/fancyhdr-it/README
%doc %{_texmfdistdir}/doc/latex/fancyhdr-it/itfancyhdr.pdf
%doc %{_texmfdistdir}/doc/latex/fancyhdr-it/itfancyhdr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110401-2
+ Revision: 751756
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110401-1
+ Revision: 718413
- texlive-fancyhdr-it
- texlive-fancyhdr-it
- texlive-fancyhdr-it
- texlive-fancyhdr-it

