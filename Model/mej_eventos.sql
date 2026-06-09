-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 13/05/2026 às 02:41
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mej_eventos`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `agenda`
--

CREATE TABLE `agenda` (
  `id` int(11) NOT NULL,
  `data_evento` date NOT NULL,
  `data_agendamento` timestamp NOT NULL DEFAULT current_timestamp(),
  `nome_evento` varchar(150) DEFAULT NULL,
  `descricao` varchar(700) DEFAULT NULL,
  `id_contratante` int(11) DEFAULT NULL,
  `id_artista` int(11) DEFAULT NULL,
  `id_local` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `agenda`
--

INSERT INTO `agenda` (`id`, `data_evento`, `data_agendamento`, `nome_evento`, `descricao`, `id_contratante`, `id_artista`, `id_local`) VALUES
(1, '2025-08-15', '2026-05-13 00:31:42', 'Festival Cultural de Inverno', 'Evento multicultural com shows, gastronomia e exposições regionais', 1, 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `artista`
--

CREATE TABLE `artista` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cnpj` varchar(20) NOT NULL,
  `contatos` varchar(300) NOT NULL,
  `endereco` varchar(500) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  `preferencias` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `artista`
--

INSERT INTO `artista` (`id`, `nome`, `cnpj`, `contatos`, `endereco`, `descricao`, `preferencias`) VALUES
(1, 'Banda Harmonia', '98.765.432/0001-11', 'harmonia@email.com | (49) 98888-0002', 'Av. Central, 250 - Chapecó/SC', 'Banda de pagode e samba com 10 anos de experiência', 'Camarim climatizado, refeição inclusa, palco mínimo 8x6m');

-- --------------------------------------------------------

--
-- Estrutura para tabela `contratante`
--

CREATE TABLE `contratante` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cnpj` varchar(20) NOT NULL,
  `contatos` varchar(300) NOT NULL,
  `endereco` varchar(500) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  `data_evento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `contratante`
--

INSERT INTO `contratante` (`id`, `nome`, `cnpj`, `contatos`, `endereco`, `descricao`, `data_evento`) VALUES
(1, 'Empresa Alpha Ltda', '12.345.678/0001-99', 'contato@alpha.com | (49) 99999-0001', 'Rua das Flores, 100 - Concórdia/SC', 'Empresa organizadora de eventos corporativos', '2025-08-15');

-- --------------------------------------------------------

--
-- Estrutura para tabela `despesas`
--

CREATE TABLE `despesas` (
  `id` int(11) NOT NULL,
  `custo_contratacao` double(15,2) DEFAULT NULL,
  `custo_local` double(15,2) DEFAULT NULL,
  `custo_equipe` double(15,2) DEFAULT NULL,
  `logistica` double(10,2) DEFAULT NULL,
  `equipamento` double(15,2) DEFAULT NULL,
  `id_contratante` int(11) DEFAULT NULL,
  `id_artista` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `despesas`
--

INSERT INTO `despesas` (`id`, `custo_contratacao`, `custo_local`, `custo_equipe`, `logistica`, `equipamento`, `id_contratante`, `id_artista`) VALUES
(1, 15000.00, 8000.00, 4500.00, 2000.00, 3500.00, 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipe`
--

CREATE TABLE `equipe` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `funcao` varchar(80) NOT NULL,
  `contato` varchar(300) DEFAULT NULL,
  `data_contratacao` date DEFAULT NULL,
  `valor_diaria` double(10,2) DEFAULT NULL,
  `observacao` varchar(500) DEFAULT NULL,
  `id_contratante` int(11) DEFAULT NULL,
  `id_despesas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `equipe`
--

INSERT INTO `equipe` (`id`, `nome`, `cpf`, `funcao`, `contato`, `data_contratacao`, `valor_diaria`, `observacao`, `id_contratante`, `id_despesas`) VALUES
(1, 'Carlos Mendes', '123.456.789-00', 'Coordenador de Palco', 'carlos.mendes@email.com | (49) 97777-5566', '2025-07-01', 350.00, 'Responsável pelo controle técnico do palco principal', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `financeiro`
--

CREATE TABLE `financeiro` (
  `id` int(11) NOT NULL,
  `id_despesas` int(11) DEFAULT NULL,
  `valor_evento` double(15,2) DEFAULT NULL,
  `metodo_pagamento` varchar(50) DEFAULT NULL,
  `despesa_total` double(15,2) DEFAULT NULL,
  `lucro_evento` double(15,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `financeiro`
--

INSERT INTO `financeiro` (`id`, `id_despesas`, `valor_evento`, `metodo_pagamento`, `despesa_total`, `lucro_evento`) VALUES
(1, 1, 50000.00, 'Transferência Bancária', 33000.00, 17000.00);

-- --------------------------------------------------------

--
-- Estrutura para tabela `local_realizado`
--

CREATE TABLE `local_realizado` (
  `id` int(11) NOT NULL,
  `nome_local` varchar(150) NOT NULL,
  `capacidade_total` int(11) DEFAULT NULL,
  `barracas_vendas` varchar(150) DEFAULT NULL,
  `endereco` varchar(300) DEFAULT NULL,
  `contato_responsavel` varchar(500) DEFAULT NULL,
  `id_contratante` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `local_realizado`
--

INSERT INTO `local_realizado` (`id`, `nome_local`, `capacidade_total`, `barracas_vendas`, `endereco`, `contato_responsavel`, `id_contratante`) VALUES
(1, 'Parque de Eventos Central', 5000, 'Alimentação, Bebidas, Artesanato', 'Rodovia SC-283, Km 10 - Concórdia/SC', 'João Silva | (49) 99111-2233', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `marketing`
--

CREATE TABLE `marketing` (
  `id` int(11) NOT NULL,
  `meio_comunicacao` varchar(100) NOT NULL,
  `tipo_midia` varchar(80) DEFAULT NULL,
  `data_inicio` date DEFAULT NULL,
  `data_fim` date DEFAULT NULL,
  `custo` double(10,2) DEFAULT NULL,
  `alcance` int(11) DEFAULT NULL,
  `id_equipe` int(11) DEFAULT NULL,
  `id_contratante` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `marketing`
--

INSERT INTO `marketing` (`id`, `meio_comunicacao`, `tipo_midia`, `data_inicio`, `data_fim`, `custo`, `alcance`, `id_equipe`, `id_contratante`) VALUES
(1, 'Redes Sociais', 'Digital - Instagram e Facebook', '2025-06-01', '2025-08-14', 2500.00, 80000, 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `patrocinadores`
--

CREATE TABLE `patrocinadores` (
  `id` int(11) NOT NULL,
  `nome_empresa` varchar(300) NOT NULL,
  `cnpj` varchar(20) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  `contato` varchar(300) DEFAULT NULL,
  `valor_patrocinio` double(15,5) DEFAULT NULL,
  `id_contratante` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `patrocinadores`
--

INSERT INTO `patrocinadores` (`id`, `nome_empresa`, `cnpj`, `descricao`, `contato`, `valor_patrocinio`, `id_contratante`) VALUES
(1, 'Cooperativa Regional', '11.222.333/0001-44', 'Patrocinadora master do evento', 'marketing@coop.com.br | (49) 3333-4444', 10000.00000, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `publico`
--

CREATE TABLE `publico` (
  `id` int(11) NOT NULL,
  `publico_alvo` varchar(50) DEFAULT NULL,
  `ingresso_vendido` int(11) DEFAULT NULL,
  `observascao` varchar(700) DEFAULT NULL,
  `faixa_etaria` varchar(20) DEFAULT NULL,
  `tipo_ingresso` varchar(50) DEFAULT NULL,
  `id_contratante` int(11) DEFAULT NULL,
  `id_artista` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `publico`
--

INSERT INTO `publico` (`id`, `publico_alvo`, `ingresso_vendido`, `observascao`, `faixa_etaria`, `tipo_ingresso`, `id_contratante`, `id_artista`) VALUES
(1, 'Família', 3200, 'Público predominantemente local e regional', '18-45 anos', 'Inteira / Meia-entrada', 1, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `agenda`
--
ALTER TABLE `agenda`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_artista` (`id_artista`),
  ADD KEY `id_contratante` (`id_contratante`),
  ADD KEY `id_local` (`id_local`);

--
-- Índices de tabela `artista`
--
ALTER TABLE `artista`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `contratante`
--
ALTER TABLE `contratante`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `despesas`
--
ALTER TABLE `despesas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_artista` (`id_artista`),
  ADD KEY `id_contratante` (`id_contratante`);

--
-- Índices de tabela `equipe`
--
ALTER TABLE `equipe`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_despesas` (`id_despesas`),
  ADD KEY `id_contratante` (`id_contratante`);

--
-- Índices de tabela `financeiro`
--
ALTER TABLE `financeiro`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_despesas` (`id_despesas`);

--
-- Índices de tabela `local_realizado`
--
ALTER TABLE `local_realizado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_contratante` (`id_contratante`);

--
-- Índices de tabela `marketing`
--
ALTER TABLE `marketing`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_equipe` (`id_equipe`),
  ADD KEY `id_contratante` (`id_contratante`);

--
-- Índices de tabela `patrocinadores`
--
ALTER TABLE `patrocinadores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_contratante` (`id_contratante`);

--
-- Índices de tabela `publico`
--
ALTER TABLE `publico`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_artista` (`id_artista`),
  ADD KEY `id_contratante` (`id_contratante`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `agenda`
--
ALTER TABLE `agenda`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `artista`
--
ALTER TABLE `artista`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `contratante`
--
ALTER TABLE `contratante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `despesas`
--
ALTER TABLE `despesas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `equipe`
--
ALTER TABLE `equipe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `financeiro`
--
ALTER TABLE `financeiro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `local_realizado`
--
ALTER TABLE `local_realizado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `marketing`
--
ALTER TABLE `marketing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `patrocinadores`
--
ALTER TABLE `patrocinadores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `publico`
--
ALTER TABLE `publico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `agenda`
--
ALTER TABLE `agenda`
  ADD CONSTRAINT `agenda_ibfk_1` FOREIGN KEY (`id_artista`) REFERENCES `artista` (`id`),
  ADD CONSTRAINT `agenda_ibfk_2` FOREIGN KEY (`id_contratante`) REFERENCES `contratante` (`id`),
  ADD CONSTRAINT `agenda_ibfk_3` FOREIGN KEY (`id_local`) REFERENCES `local_realizado` (`id`);

--
-- Restrições para tabelas `despesas`
--
ALTER TABLE `despesas`
  ADD CONSTRAINT `despesas_ibfk_1` FOREIGN KEY (`id_artista`) REFERENCES `artista` (`id`),
  ADD CONSTRAINT `despesas_ibfk_2` FOREIGN KEY (`id_contratante`) REFERENCES `contratante` (`id`);

--
-- Restrições para tabelas `equipe`
--
ALTER TABLE `equipe`
  ADD CONSTRAINT `equipe_ibfk_1` FOREIGN KEY (`id_despesas`) REFERENCES `despesas` (`id`),
  ADD CONSTRAINT `equipe_ibfk_2` FOREIGN KEY (`id_contratante`) REFERENCES `contratante` (`id`);

--
-- Restrições para tabelas `financeiro`
--
ALTER TABLE `financeiro`
  ADD CONSTRAINT `financeiro_ibfk_1` FOREIGN KEY (`id_despesas`) REFERENCES `despesas` (`id`);

--
-- Restrições para tabelas `local_realizado`
--
ALTER TABLE `local_realizado`
  ADD CONSTRAINT `local_realizado_ibfk_1` FOREIGN KEY (`id_contratante`) REFERENCES `contratante` (`id`);

--
-- Restrições para tabelas `marketing`
--
ALTER TABLE `marketing`
  ADD CONSTRAINT `marketing_ibfk_1` FOREIGN KEY (`id_equipe`) REFERENCES `equipe` (`id`),
  ADD CONSTRAINT `marketing_ibfk_2` FOREIGN KEY (`id_contratante`) REFERENCES `contratante` (`id`);

--
-- Restrições para tabelas `patrocinadores`
--
ALTER TABLE `patrocinadores`
  ADD CONSTRAINT `patrocinadores_ibfk_1` FOREIGN KEY (`id_contratante`) REFERENCES `contratante` (`id`);

--
-- Restrições para tabelas `publico`
--
ALTER TABLE `publico`
  ADD CONSTRAINT `publico_ibfk_1` FOREIGN KEY (`id_artista`) REFERENCES `artista` (`id`),
  ADD CONSTRAINT `publico_ibfk_2` FOREIGN KEY (`id_contratante`) REFERENCES `contratante` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


create view view_agenda_artista as 
select a.nome, a.contatos, a.preferencias, a.descricao as artista, agen.data_evento, agen.nome_evento from agenda agen inner join artista a on agen.id_artista = a.id;

create view view_agenda_local as
select l.nome_local, l.capacidade_total,l.endereco as local_realizado, a.data_evento, a.nome_evento, a.descricao FROM agenda a INNER JOIN local_realizado l ON a.id_local = l.id;

create view view_contratante_equipe as
select c.nome, c.contatos, c.descricao as contratante, e.nome,e.funcao,e.contato from equipe e left join contratante c on e.id_contratante = c.id;

create view view_contratante_marketing as
select c.nome, c.contatos, c.descricao as contratante, m.meio_comunicacao, m.tipo_midia, m.custo from marketing m left join contratante c on m.id_contratante = c.id;