-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 22, 2025 at 10:52 AM
-- Server version: 8.4.3
-- PHP Version: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`id`, `kode_anggota`, `nama`, `alamat`, `telepon`, `email`, `created_at`, `updated_at`) VALUES
(1, 'A001', 'Budi Santoso', 'Jl. Merdeka No. 10', '08121234501', 'budi.santoso@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(2, 'A002', 'Citra Kirana', 'Jl. Sudirman Gg. 5', '08132345602', 'citra.kirana@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(3, 'A003', 'Dedi Iskandar', 'Perumahan Indah Blok C3', '08573456703', 'dedi.iskandar@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(4, 'A004', 'Eka Lestari', 'Jl. Pahlawan No. 25', '08784567804', 'eka.lestari@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(5, 'A005', 'Fahmi Wijaya', 'Komplek Damai Blok H', '08965678905', 'fahmi.wijaya@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(6, 'A006', 'Gita Permata', 'Jl. Nusantara Km. 2', '08126789006', 'gita.permata@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(7, 'A007', 'Hendra Setiawan', 'Griya Sejahtera No. 15', '08137890107', 'hendra.setiawan@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(8, 'A008', 'Intan Sari', 'Jl. Mawar No. 40', '08578901208', 'intan.sari@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(9, 'A009', 'Joko Susilo', 'Desa Mekar Sari RT 01', '08789012309', 'joko.susilo@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(10, 'A010', 'Kiki Amelia', 'Jalan Baru No. 11A', '08960123410', 'kiki.amelia@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(11, 'A011', 'Lina Marlina', 'Jl. Kencana No. 5', '08121234511', 'lina.marlina@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(12, 'A012', 'Maman Abdurrahman', 'Perum Asri Blok A1', '08132345612', 'maman.abdurrahman@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(13, 'A013', 'Nina Zulkarnaen', 'Jalan Raya Timur Km. 10', '08573456713', 'nina.zulkarnaen@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(14, 'A014', 'Oki Pramana', 'Jl. Anggrek No. 17', '08784567814', 'oki.pramana@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(15, 'A015', 'Putri Diana', 'Komplek Harapan Indah', '08965678915', 'putri.diana@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(16, 'A016', 'Rizal Fachri', 'Jl. Cemara No. 8', '08126789016', 'rizal.fachri@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(17, 'A017', 'Siska Dewi', 'Gg. Melati No. 3', '08137890117', 'siska.dewi@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(18, 'A018', 'Taufik Hidayat', 'Perumahan Hijau Blok F4', '08578901218', 'taufik.hidayat@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(19, 'A019', 'Umi Kulsum', 'Jalan Sepakat No. 22', '08789012319', 'umi.kulsum@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(20, 'A020', 'Vicky Prasetyo', 'Komplek Permai A5', '08960123420', 'vicky.prasetyo@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(21, 'A021', 'Wulan Guritno', 'Jl. Tentara Pelajar No. 7', '08121234521', 'wulan.guritno@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(22, 'A022', 'Yuni Shara', 'Desa Sukamaju RT 03', '08132345622', 'yuni.shara@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(23, 'A023', 'Zainal Arifin', 'Jl. Kelapa Dua No. 9', '08573456723', 'zainal.arifin@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(24, 'A024', 'Ani Cahyani', 'Perum Elok Blok G1', '08784567824', 'ani.cahyani@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(25, 'A025', 'Bima Sakti', 'Jalan Kenanga No. 12', '08965678925', 'bima.sakti@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(26, 'A026', 'Cinta Laura', 'Komplek Cendana No. 2', '08126789026', 'cinta.laura@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(27, 'A027', 'Denny Cagur', 'Gg. H. Ramli No. 10', '08137890127', 'denny.cagur@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(28, 'A028', 'Erwin Riyadi', 'Jl. Bambu Apus 1', '08578901228', 'erwin.riyadi@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(29, 'A029', 'Fara Diba', 'Perumahan Bukit Mas', '08789012329', 'fara.diba@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(30, 'A030', 'Gading Marten', 'Jalan Pramuka No. 1', '08960123430', 'gading.marten@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(31, 'A031', 'Hesti Purwadinata', 'Komplek Puri Kencana', '08121234531', 'hesti.purwadinata@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(32, 'A032', 'Irfan Hakim', 'Jl. Petani Raya No. 14', '08132345632', 'irfan.hakim@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(33, 'A033', 'Jessica Mila', 'Gg. Mangga No. 6', '08573456733', 'jessica.mila@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(34, 'A034', 'Kevin Julio', 'Perumahan Pelangi Indah', '08784567834', 'kevin.julio@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(35, 'A035', 'Luna Maya', 'Jl. Cempaka Putih No. 3', '08965678935', 'luna.maya@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(36, 'A036', 'Mario Teguh', 'Komplek Mutiara 1', '08126789036', 'mario.teguh@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(37, 'A037', 'Nia Ramadhani', 'Jalan Garuda No. 18', '08137890137', 'nia.ramadhani@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(38, 'A038', 'Oni Syahrial', 'Perum Taman Sari C2', '08578901238', 'oni.syahrial@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(39, 'A039', 'Pandji Pragiwaksono', 'Jl. Veteran No. 30', '08789012339', 'pandji.pragiwaksono@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(40, 'A040', 'Qory Sandioriva', 'Komplek Permata Biru', '08960123440', 'qory.sandioriva@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(41, 'A041', 'Raisa Andriana', 'Jalan Haji Nawi No. 20', '08121234541', 'raisa.andriana@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(42, 'A042', 'Rio Dewanto', 'Gg. Kenari No. 8', '08132345642', 'rio.dewanto@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(43, 'A043', 'Sandra Dewi', 'Perumahan Citra Raya', '08573456743', 'sandra.dewi@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(44, 'A044', 'Tulus Rusydi', 'Jl. Siliwangi No. 19', '08784567844', 'tulus.rusydi@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(45, 'A045', 'Uus Sebenarnya', 'Komplek Griya Asri', '08965678945', 'uus.sebenarnya@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(46, 'A046', 'Vina Panduwinata', 'Jalan Kaki Lima No. 2', '08126789046', 'vina.panduwinata@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(47, 'A047', 'Wali Band', 'Gg. Lurus No. 1', '08137890147', 'wali.band@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(48, 'A048', 'Xena Siregar', 'Perumahan Harmoni E5', '08578901248', 'xena.siregar@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(49, 'A049', 'Yoga Pratama', 'Jl. Danau Sunter No. 5', '08789012349', 'yoga.pratama@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51'),
(50, 'A050', 'Zaskia Adya Mecca', 'Komplek Bintang Timur', '08960123450', 'zaskia.adya.mecca@email.com', '2025-10-22 09:02:51', '2025-10-22 09:02:51');

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id`, `kode_buku`, `judul`, `pengarang`, `penerbit`, `tahun_terbit`, `stok`, `created_at`, `updated_at`) VALUES
(1, 'B001', 'Laskar Pelangi', 'Andrea Hirata', 'Bentang Pustaka', 2005, 15, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(2, 'B002', 'Perahu Kertas', 'Dee Lestari', 'Bentang Pustaka', 2009, 20, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(3, 'B003', 'Negeri 5 Menara', 'Ahmad Fuadi', 'Gramedia Pustaka Utama', 2009, 10, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(4, 'B004', 'Ayat-Ayat Cinta', 'Habiburrahman El Shirazy', 'Republika', 2004, 25, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(5, 'B005', 'Dilan: Dia Adalah Dilanku Tahun 1990', 'Pidi Baiq', 'Pastel Books', 2014, 30, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(6, 'B006', 'Bumi Manusia', 'Pramoedya Ananta Toer', 'Hasta Mitra', 1980, 12, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(7, 'B007', 'Sang Pemimpi', 'Andrea Hirata', 'Bentang Pustaka', 2006, 18, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(8, 'B008', 'Filosofi Kopi', 'Dee Lestari', 'Truedee Books', 2006, 8, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(9, 'B009', 'Ronggeng Dukuh Paruk', 'Ahmad Tohari', 'Gramedia Pustaka Utama', 1982, 11, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(10, 'B010', 'Cantik Itu Luka', 'Eka Kurniawan', 'Gramedia Pustaka Utama', 2002, 14, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(11, 'B011', 'The Kite Runner', 'Khaled Hosseini', 'Riverhead Books', 2003, 16, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(12, 'B012', 'The Lord of the Rings', 'J.R.R. Tolkien', 'Allen & Unwin', 1954, 7, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(13, 'B013', 'Harry Potter dan Batu Bertuah', 'J.K. Rowling', 'Scholastic', 1997, 22, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(14, 'B014', 'Atomic Habits', 'James Clear', 'Avery', 2018, 40, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(15, 'B015', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'Harper', 2011, 28, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(16, 'B016', 'Self-Healing is For Everyone', 'Deassy M. Maryono', 'Elex Media Komputindo', 2020, 19, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(17, 'B017', 'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Warner Books', 1997, 35, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(18, 'B018', 'Sebuah Seni Untuk Bersikap Bodo Amat', 'Mark Manson', 'HarperOne', 2016, 27, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(19, 'B019', 'Teori Bilangan', 'Eko Budi Prasetyo', 'Penerbit ITB', 2015, 6, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(20, 'B020', 'Dasar-Dasar Pemrograman Python', 'Romi Satria Wahono', 'IAII', 2019, 13, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(21, 'B021', 'Kalkulus Lanjut', 'Purwanto', 'Erlangga', 2010, 9, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(22, 'B022', 'Fisika Dasar Jilid 1', 'Halliday dan Resnick', 'Wiley', 1960, 15, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(23, 'B023', 'Kimia Organik', 'Fessenden & Fessenden', 'Erlangga', 1982, 10, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(24, 'B024', 'Ekonomi Mikro', 'N. Gregory Mankiw', 'Cengage Learning', 1998, 20, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(25, 'B025', 'Pengantar Ilmu Politik', 'Miriam Budiardjo', 'Gramedia Pustaka Utama', 2008, 17, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(26, 'B026', 'Sejarah Nasional Indonesia Jilid 6', 'Marwati Djoened Poesponegoro', 'Balai Pustaka', 1984, 8, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(27, 'B027', 'Psikologi Pendidikan', 'Muhibbin Syah', 'Remaja Rosdakarya', 2003, 11, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(28, 'B028', 'Metodologi Penelitian Kuantitatif', 'Sugiyono', 'Alfabeta', 2018, 25, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(29, 'B029', 'Statistika Non-Parametrik', 'Sidney Siegel', 'McGraw-Hill', 1956, 14, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(30, 'B030', 'Jaringan Komputer', 'Andrew S. Tanenbaum', 'Prentice Hall', 2003, 16, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(31, 'B031', 'Belajar Sendiri HTML dan CSS', 'Jubilee Enterprise', 'Elex Media Komputindo', 2021, 30, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(32, 'B032', 'Mahir Javascript Modern', 'Rahmat Hidayat', 'Informatika', 2020, 22, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(33, 'B033', 'Koding itu Mudah: C#', 'Adi Nugroho', 'Andi Publisher', 2017, 18, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(34, 'B034', 'Data Science dengan Python', 'Muhammad Afif', 'Gramedia', 2022, 15, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(35, 'B035', 'Artificial Intelligence: A Modern Approach', 'Stuart Russell', 'Prentice Hall', 2010, 10, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(36, 'B036', 'Hujan', 'Tere Liye', 'Gramedia Pustaka Utama', 2016, 29, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(37, 'B037', 'Pulang', 'Tere Liye', 'Gramedia Pustaka Utama', 2015, 23, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(38, 'B038', 'Laut Bercerita', 'Leila S. Chudori', 'Kepustakaan Populer Gramedia', 2017, 12, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(39, 'B039', 'Garis Waktu', 'Fiersa Besari', 'Media Kita', 2016, 32, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(40, 'B040', '1984', 'George Orwell', 'Secker & Warburg', 1949, 17, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(41, 'B041', 'To Kill a Mockingbird', 'Harper Lee', 'J. B. Lippincott & Co.', 1960, 9, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(42, 'B042', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Charles Scribner\'s Sons', 1925, 13, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(43, 'B043', 'Pride and Prejudice', 'Jane Austen', 'T. Egerton, Whitehall', 1813, 11, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(44, 'B044', 'One Hundred Years of Solitude', 'Gabriel García Márquez', 'Editorial Sudamericana', 1967, 14, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(45, 'B045', 'The Alchemist', 'Paulo Coelho', 'HarperOne', 1988, 26, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(46, 'B046', 'Marmut Merah Jambu', 'Raditya Dika', 'GagasMedia', 2010, 31, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(47, 'B047', 'Kambing Jantan', 'Raditya Dika', 'GagasMedia', 2005, 24, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(48, 'B048', 'Berjuta Rasanya', 'Trinity', 'Elex Media Komputindo', 2016, 19, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(49, 'B049', 'Traveling: Jurnal Cepat', 'Dewi Lestari', 'Bentang Pustaka', 2021, 15, '2025-10-22 09:04:20', '2025-10-22 09:04:20'),
(50, 'B050', 'Resep Masakan Nusantara Lengkap', 'Bara Pattiradjawane', 'Gramedia', 2018, 20, '2025-10-22 09:04:20', '2025-10-22 09:04:20');

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `created_at`, `updated_at`) VALUES
(1, 'admin', '123', 'admin', '2025-10-22 05:41:51', '2025-10-22 05:41:51'),
(2, 'petugas', 'petugas123', 'staff', '2025-10-22 05:42:39', '2025-10-22 05:42:39'),
(3, 'member', 'member123', 'user', '2025-10-22 05:42:39', '2025-10-22 05:42:39');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
