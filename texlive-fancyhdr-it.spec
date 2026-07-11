%global tl_name fancyhdr-it
%global tl_revision 21912

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Italian translation of fancyhdr documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/fancyhdr/it
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr-it.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr-it.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The translation is of documentation provided with the fancyhdr package.

