

--Cleaning Data in SQL Queries

select*
from NashvilleHousing



--Standardize Date Format

select SaleDateConverted,CONVERT(Date,SaleDate)
from NashvilleHousing


Update NashvilleHousing
Set SaleDate = CONVERT(Date,SaleDate)


Alter Table NashvilleHousing
Add SaleDateConverted Date ;

Update NashvilleHousing
Set SaleDateConverted = CONVERT(Date,SaleDate)



--Populate Property Address Data

Select *
From NashvilleHousing
order by ParcelID



Select a.parcelID, a.propertyaddress, b.parcelID, b.propertyaddress, ISNULL(a.propertyaddress,b.propertyaddress)
from NashvilleHousing a
Join NashvilleHousing b
on a.parcelID = b.parcelID
and a.uniqueID <> b.uniqueID
where a.propertyaddress is null


Update a
SET propertyaddress = ISNULL(a.propertyaddress,b.propertyaddress)
from NashvilleHousing a
Join NashvilleHousing b
on a.parcelID = b.parcelID
and a.uniqueID <> b.uniqueID
where a.propertyaddress is null



--Breaking out Address into Individual Columns (Address, City, Date)
select PropertyAddress address
from NashvilleHousing


SELECT
SUBSTRING(propertyaddress, 1, CHARINDEX(',', propertyaddress) -1 ) as Address
, SUBSTRING(propertyaddress, CHARINDEX(',', propertyaddress) + 1 , LEN(propertyaddress)) as Address

From NashvilleHousing


ALTER TABLE NashvilleHousing
Add PropertySplitAddress Nvarchar(255);

Update NashvilleHousing
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 )


ALTER TABLE NashvilleHousing
Add PropertySplitCity Nvarchar(255);

Update NashvilleHousing
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))




Select *
From NashvilleHousing





Select OwnerAddress
From NashvilleHousing


Select
PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)
From NashvilleHousing



ALTER TABLE NashvilleHousing
Add OwnerSplitAddress Nvarchar(255);

Update NashvilleHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)


ALTER TABLE NashvilleHousing
Add OwnerSplitCity Nvarchar(255);

Update NashvilleHousing
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)



ALTER TABLE NashvilleHousing
Add OwnerSplitState Nvarchar(255);

Update NashvilleHousing
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)



Select *
From NashvilleHousing



--Change Y and N to Yes and No in "Sold As Vacant" field

select distinct(soldasvacant),count(soldasvacant)
from NashvilleHousing
group by soldasvacant
order by 2

select soldasvacant
,	case
	when soldasvacant = 'Y' then 'Yes'
	when soldasvacant = 'N' then 'No'
	else soldasvacant
	end
from NashvilleHousing


update NashvilleHousing
SET SoldAsVacant = case 
	when soldasvacant = 'Y' then 'Yes'
	when soldasvacant = 'N' then 'No'
	else soldasvacant
	end



--Remove Duplicates



With ROW_NUMCTE as(
select *,
	ROW_NUMBER() over (
	partition by parcelID,
	Propertyaddress,
	Saleprice,
	Saledate,
	Legalreference
	order by
		uniqueID
		) row_num
from NashvilleHousing
)
--delete
--from ROW_NUMCTE
--where row_num > 1

select *
from ROW_NUMCTE
where row_num > 1
order by PropertyAddress



--Delete Unused Columns


select*
from NashvilleHousing

Alter Table NashvilleHousing
Drop Column owneraddress,taxdistrict,propertyaddress,saledate
