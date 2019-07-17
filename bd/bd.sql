-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 03-Jun-2019 às 15:14
-- Versão do servidor: 5.7.23
-- versão do PHP: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `contato`
--

DROP TABLE IF EXISTS `contato`;
CREATE TABLE IF NOT EXISTS `contato` (
  `codcontato` int(10) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `ativo` char(1) NOT NULL,
  `cadastro` char(1) NOT NULL,
  `codusuario` int(11) NOT NULL,
  `data` datetime NOT NULL DEFAULT '2011-01-26 14:30:00',
  PRIMARY KEY (`codcontato`)
) ENGINE=MyISAM AUTO_INCREMENT=82 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `contato`
--

INSERT INTO `contato` (`codcontato`, `nome`, `ativo`, `cadastro`, `codusuario`, `data`) VALUES
(71, 'todos', 'S', 'S', 0, '2019-06-02 16:18:34'),
(81, 'todos', 'S', 'S', 2, '2019-06-02 16:45:13'),
(80, 'todos', 'S', 'S', 1, '2019-06-02 16:43:44');

-- --------------------------------------------------------

--
-- Estrutura da tabela `imagem`
--

DROP TABLE IF EXISTS `imagem`;
CREATE TABLE IF NOT EXISTS `imagem` (
  `codimagem` int(10) NOT NULL AUTO_INCREMENT,
  `codusuario` int(10) NOT NULL,
  `imagem` longblob NOT NULL,
  PRIMARY KEY (`codimagem`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `interacao`
--

DROP TABLE IF EXISTS `interacao`;
CREATE TABLE IF NOT EXISTS `interacao` (
  `codinteracao` int(10) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(10) NOT NULL,
  `entrada` varchar(100) NOT NULL,
  `ativo` char(1) NOT NULL,
  `codusuario` int(10) DEFAULT NULL,
  PRIMARY KEY (`codinteracao`)
) ENGINE=MyISAM AUTO_INCREMENT=84 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `interacao`
--

INSERT INTO `interacao` (`codinteracao`, `tipo`, `entrada`, `ativo`, `codusuario`) VALUES
(2, '$', 'listar comandos', 'S', 1),
(1, '$', 'listar comandos', 'S', 0),
(3, '$', 'listar comandos', 'S', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `codlogin` int(10) NOT NULL AUTO_INCREMENT,
  `codusuario` int(10) NOT NULL,
  `start` char(1) NOT NULL,
  `data` datetime(6) NOT NULL,
  PRIMARY KEY (`codlogin`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `parametros`
--

DROP TABLE IF EXISTS `parametros`;
CREATE TABLE IF NOT EXISTS `parametros` (
  `codparametros` int(11) NOT NULL AUTO_INCREMENT,
  `data` varchar(20) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `obs` varchar(100) DEFAULT NULL,
  `parametro` varchar(100) DEFAULT NULL,
  `ativo` char(1) NOT NULL,
  `editavel` char(1) NOT NULL,
  `codusuario` int(10) NOT NULL,
  PRIMARY KEY (`codparametros`)
) ENGINE=MyISAM AUTO_INCREMENT=247 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `parametros`
--

INSERT INTO `parametros` (`codparametros`, `data`, `tipo`, `obs`, `parametro`, `ativo`, `editavel`, `codusuario`) VALUES
(3, '11/05/2019 18:52:00', '@', 'Conversação', 'C', '', 'N', 0),
(4, '11/05/2019 18:52:00', '>', 'comandos por scripts', 'S', '', 'N', 0),
(5, '11/05/2019 18:52:00', '<', 'comandos por script com retorno', 'S', '', 'N', 0),
(6, '11/05/2019 18:52:00', '-', 'comandos diretos para o terminal com retorno', 'S', '', 'N', 0),
(7, '11/05/2019 18:52:00', '=', 'comandos especiais programados/fixos', 'S', '', 'N', 0),
(236, '2019-06-02 16:39:56', 'T', 'Ativa novos cadastros', 'addcontato', 'N', 'S', 0),
(235, '2019-06-02 16:39:56', 'S', 'Servidor de execução', 'servconv', 'N', 'S', 0),
(241, '2019-06-02 16:43:44', 'T', 'Ativa novos cadastros', 'addcontato', 'N', 'S', 1),
(237, '2019-06-02 16:39:56', 'C', 'Servidor de respostas', 'servconv', 'N', 'S', 0),
(242, '2019-06-02 16:43:44', 'S', 'Servidor de execução', 'servconv', 'N', 'S', 1),
(243, '2019-06-02 16:43:44', 'C', 'Servidor de respostas', 'servconv', 'N', 'S', 1),
(244, '2019-06-02 16:45:13', 'T', 'Ativa novos cadastros', 'addcontato', 'N', 'S', 2),
(245, '2019-06-02 16:45:13', 'S', 'Servidor de execução', 'servconv', 'N', 'S', 2),
(246, '2019-06-02 16:45:13', 'C', 'Servidor de respostas', 'servconv', 'N', 'S', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `saida`
--

DROP TABLE IF EXISTS `saida`;
CREATE TABLE IF NOT EXISTS `saida` (
  `codsaida` int(10) NOT NULL,
  `codinteracao` int(10) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `saida` varchar(500) NOT NULL,
  `ativo` char(1) NOT NULL,
  PRIMARY KEY (`codinteracao`,`codsaida`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `saida`
--

INSERT INTO `saida` (`codsaida`, `codinteracao`, `tipo`, `saida`, `ativo`) VALUES
(1, 1, '=', 'Registro fixo do sistema', 'S'),
(1, 3, '=', 'Registro fixo do sistema', 'S'),
(1, 2, '=', 'Registro fixo do sistema', 'S');

-- --------------------------------------------------------

--
-- Estrutura da tabela `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) COLLATE utf8_bin NOT NULL,
  `password` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `codusuario` int(10) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(100) NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `ativo` char(1) NOT NULL,
  `cod` int(10) NOT NULL,
  `data` datetime(6) NOT NULL,
  PRIMARY KEY (`codusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`codusuario`, `nome`, `email`, `senha`, `telefone`, `ativo`, `cod`, `data`) VALUES
(0, 'admin', 'admin', 'admin', 21980317641, 'S', 0, '2019-05-30 00:00:00.000000'),
(1, 'Mauricio Rodrigues da Silva', 'mauriciosist@gmail.com', '123', 2126357344, 'S', 0, '2019-06-02 16:43:44.000000'),
(2, 'Marihá dos Santos Carvalho Rodrigues', 'marihacarvalho@gmail.com', '123', 21967003545, 'S', 1, '2019-06-02 16:45:13.000000');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
