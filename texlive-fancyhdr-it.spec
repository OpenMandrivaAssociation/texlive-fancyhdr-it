Name:		texlive-fancyhdr-it
Version:	20180303
Release:	2
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
%doc %{_texmfdistdir}/doc/latex/fancyhdr-it

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
