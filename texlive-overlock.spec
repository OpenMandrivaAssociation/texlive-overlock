Name:		texlive-overlock
Version:	64495
Release:	2
Summary:	Overlock sans fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/overlock
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overlock.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overlock.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the Overlock and OverlockSC families of
fonts, designed by Dario Manuel Muhafara of the TIPO foundry
(http://www.tipo.net.ar), "rounded" sans-serif fonts in three
weights (Regular, Bold, Black) with italic variants for each of
them. There are also small-caps and old-style figures in the
Regular weight.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/overlock
%{_texmfdistdir}/fonts/vf/tipo/overlock
%{_texmfdistdir}/fonts/type1/tipo/overlock
%{_texmfdistdir}/fonts/tfm/tipo/overlock
%{_texmfdistdir}/fonts/opentype/tipo/overlock
%{_texmfdistdir}/fonts/map/dvips/overlock
%{_texmfdistdir}/fonts/enc/dvips/overlock
%doc %{_texmfdistdir}/doc/fonts/overlock

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
