# Original: https://bpaulino.com/entries/10-automating-your-work-with-github-actions
# Create working environment for running scripts

FROM ubuntu:20.04
LABEL author="Duc A. Hoang"

# Use /bin/bash instead of /bin/sh
SHELL ["/bin/bash", "-c"]

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
#ENV TZ=Asia/Ho_Chi_Minh

# Install some necessary packages
RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	build-essential \ 
	rsync \
	tree \
	locales \
	wget \
	make \ 
	git-all \ 
	gnupg2 \
	dirmngr \
	curl \ 
	ssh \ 
	secure-delete \ 
	libcurl4-openssl-dev \
	ca-certificates \
	perl \
	ruby \
	ruby-dev && \
	rm -rf /var/lib/apt/lists/*

# Set locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

# TeXLive
#COPY texlive*.profile /
#RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
#	tar xvf install-tl-unx.tar.gz && \
#	rm -rf install-tl-unx.tar.gz && \
#	cd $(basename install-tl-*) && \
#	./install-tl --profile=/texlive.profile && \
#	rm -rf /texlive.profile /install-tl-* && \
#	echo "PATH=/usr/local/texlive/2021/bin/x86_64-linux:$PATH; export PATH" >> /etc/bash.bashrc && \
#	echo "MANPATH=/usr/local/texlive/2021/texmf-dist/doc/man:$MANPATH; export MANPATH"  >> /etc/bash.bashrc && \
#	echo "INFOPATH=/usr/local/texlive/2021/texmf-dist/doc/info:$INFOPATH; export INFOPATH"  >> /etc/bash.bashrc

#RUN tlmgr update --self
#	
#RUN tlmgr install \
#		latexmk \
#		moderncv \
#		babel-vietnamese \
#		vntex \
#		biblatex \
#		biber \
#		multirow \
#		pgf \
#		arydshln \
#		bxcjkjatype cjk cjkpunct ipaex-type1

# Jekyll
RUN gem install bundler --version 2.2.25

# This is our entrypoint to our custom scripts
# more about that in a sec
COPY entrypoint.sh /

# Use the entrypoint.sh file as the container entrypoint 
# (i.e., the commands to run inside the container)
# when Github executes our Docker container
ENTRYPOINT ["bash", "/entrypoint.sh"]
