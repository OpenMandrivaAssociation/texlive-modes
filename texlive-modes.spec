Name:		texlive-modes
Version:	61719
Release:	1
Summary:	A collection of Metafont mode_def's
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modes
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The modes file collects all known Metafont modes for printing
or display devices, of whatever printing technology. Special
provision is made for write-white printers, and a 'landscape'
mode is available, for making suitable fonts for printers with
pixels whose aspect is non-square. The file also provides
definitions that make \specials identifying the mode in
Metafont's GF output, and put coding information and other
Xerox-world information in the TFM file.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/fonts/source/public/modes
%doc %{_texmfdistdir}/doc/fonts/modes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
